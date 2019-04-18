# Internal
from monit.multicast_group import MulticastGroup
from monit.publish.local_publisher import LocalPublisher
from monit.subscribe.local_subscriber import LocalSubscriber
from monit.publish.multicast_publisher import MulticastPublisher
# Python
import asyncio


class VirtualNode:

    def __init__(self, name, localSubsPort, multicastGroupIp, multicastGroupPort, ownIp, localPublishPort):

        self._name = name

        self.localSub = LocalSubscriber(localSubsPort)
        self.localSub.subscribe()

        self.localPub = LocalPublisher(localPublishPort)
        self.localPub.connect()

        self.multicastPub = MulticastPublisher(ownIp, MulticastGroup(multicastGroupIp, multicastGroupPort))
        self.multicastPub.connect()


    async def processLocal(self):

        while True:
            local = await self.localSub.process()
            print(local)
            self.handlePackage(local)

            await self.multicastPub.send(local)
            await self.localPub.send(local)


    async def processRemote(self):
        pass


    def handlePackage(self, package):
        package['path'] = '/' + self._name + package['path']


if __name__ == '__main__':

    node =  VirtualNode(name = 'prima',
                        localSubsPort = 1112,
                        multicastGroupIp = '239.1.1.1',
                        multicastGroupPort = 2222,
                        ownIp = '10.13.0.171',
                        localPublishPort = 3333)

    try:
        tasks = asyncio.gather(node.processLocal())
        asyncio.get_event_loop().run_until_complete(tasks)

    finally:
        asyncio.get_event_loop().close()
