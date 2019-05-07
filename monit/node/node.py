# Internal
from monit.data_type.deep_dict import AvkDict
from monit.data_type.multicast_group import MulticastGroup
from monit.publish.local_publisher import LocalPublisher
from monit.subscribe.local_subscriber import LocalSubscriber
from monit.publish.multicast_publisher import MulticastPublisher
from monit.subscribe.multicast_subscriber import MulticastSubscriber


class Node:

    def __init__(self, name, localSubsPort, multicastGroupIp, multicastGroupPort, ownIps, localPublishPort):

        self.avkDict = AvkDict()
        self.avkDict.deepUpdate({name: {}})

        self._name = name

        self.localSub = LocalSubscriber(localSubsPort)
        self.localSub.subscribe()

        self.localPub = LocalPublisher(localPublishPort)
        self.localPub.connect()

        self.multicastSub = MulticastSubscriber(MulticastGroup(multicastGroupIp, multicastGroupPort))
        self.multicastSub.subscribe()

        if type(ownIps) is str:
            ownIps = [ownIps]

        self.multicastPublishers = [MulticastPublisher(ownIp, MulticastGroup(multicastGroupIp, multicastGroupPort)) for ownIp in ownIps]

        for publisher in self.multicastPublishers:
            publisher.connect()


    async def processLocal(self):

        while True:

            local = await self.localSub.process()
            local = self.handlePackage(local)

            self.avkDict.deepUpdate(local)

            for publisher in self.multicastPublishers:
                await publisher.send(self.avkDict.get(self._name))

            await self.localPub.send(self.avkDict.dictionary)


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
