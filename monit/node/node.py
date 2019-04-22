# Internal
from monit.tmp.deep_dict import AvkDict
from monit.multicast_group import MulticastGroup
from monit.publish.local_publisher import LocalPublisher
from monit.subscribe.local_subscriber import LocalSubscriber
from monit.publish.multicast_publisher import MulticastPublisher
from monit.subscribe.multicast_subscriber import MulticastSubscriber
# Python
import asyncio


class Node:

    def __init__(self, name, localSubsPort, multicastGroupIp, multicastGroupPort, ownIp, localPublishPort):

        self.avkDict = AvkDict()
        self.avkDict.deepUpdate({name: {}})

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
            local = self.handlePackage(local)

            self.avkDict.deepUpdate(local)

            await self.multicastPub.send(self.avkDict.get(self._name))
            print('self.multicastPub.send', self.avkDict.get(self._name))

            await self.localPub.send(self.avkDict.dictionary)
            print('self.localPub.send', self.avkDict.dictionary)


    async def processRemote(self):

        while True:

            remote = await self.multicastSub.process()
            self.avkDict.deepUpdate(remote)

            await self.localPub.send(remote)


    def handlePackage(self, package):

        result = package['path']
        if package.get('virtual') is not True:
            result = '/' + self._name + package['path']

        result = AvkDict.convertPathToEmptyDict(result, package['state'])
        return result


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

