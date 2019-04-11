# Internal
from tmp.multicast_group import MulticastGroup
from tmp.subscribe.local_subscriber import LocalSubscriber
from tmp.publish.multicast_publisher import MulticastPublisher
from tmp.subscribe.multicast_subscriber import MulticastSubscriber
# Python
import asyncio


class Node:

    def __init__(self, name):

        self._name = name

        self.localSub = LocalSubscriber(5553)
        self.localSub.subscribe()

        self.multicastSub = MulticastSubscriber(MulticastGroup('239.1.1.1', 5554))
        self.multicastSub.subscribe()

        self.multicastPub = MulticastPublisher('10.13.0.171', MulticastGroup('239.1.1.1', 5554))
        self.multicastPub.connect()


    async def processLocal(self):

        while True:
            local = await self.localSub.process()
            await self.handlePackage(local)


    async def processRemote(self):

        while True:

            remote = await self.multicastSub.process()
            print('remote multicastPub send', remote)
            await self.multicastPub.send(remote)


    async def handlePackage(self, package):

        package['path'] = '/' + self._name + package['path']
        await self.multicastPub.send(package)
        print('self.multicastPub.send', package)


if __name__ == '__main__':

    node =  Node('client1')

    try:
        tasks = asyncio.gather(node.processLocal(), node.processRemote())
        asyncio.get_event_loop().run_until_complete(tasks)

    finally:
        asyncio.get_event_loop().close()

