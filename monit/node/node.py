# Internal
from monit.multicast_group import MulticastGroup
from monit.publish.local_publisher import LocalPublisher
from monit.subscribe.local_subscriber import LocalSubscriber
from monit.publish.multicast_publisher import MulticastPublisher
from monit.subscribe.multicast_subscriber import MulticastSubscriber
# Python
import asyncio


class Node:

    def __init__(self, name, localSubsPort, multicastGroupIp, multicastGroupPort, ownIp, localPublishPort):

        self._name = name

        self.localSub = LocalSubscriber(localSubsPort)
        self.localSub.subscribe()

        self.localPub = LocalPublisher(localPublishPort)
        self.localPub.connect()

        self.multicastSub = MulticastSubscriber(MulticastGroup(multicastGroupIp, multicastGroupPort))
        self.multicastSub.subscribe()

        self.multicastPub = MulticastPublisher(ownIp, MulticastGroup(multicastGroupIp, multicastGroupPort))
        self.multicastPub.connect()


    async def processLocal(self):

        while True:
            local = await self.localSub.process()
            await self.handlePackage(local)


    async def processRemote(self):

        while True:

            remote = await self.multicastSub.process()
            await self.localPub.send(remote)


    async def handlePackage(self, package):

        package['path'] = '/' + self._name + package['path']

        await self.multicastPub.send(package)
        await self.localPub.send(package)


if __name__ == '__main__':

    node =  Node(name = 'client1',
                 localSubsPort = 1111,
                 multicastGroupIp = '239.1.1.1',
                 multicastGroupPort = 2222,
                 ownIp = '10.13.0.171',
                 localPublishPort = 3333)

    try:
        tasks = asyncio.gather(node.processLocal(), node.processRemote())
        asyncio.get_event_loop().run_until_complete(tasks)

    finally:
        asyncio.get_event_loop().close()

