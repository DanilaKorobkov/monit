# Internal
from tmp.multicast_group import MulticastGroup
from tmp.subscribe.local_subscriber import LocalSubscriber
from tmp.publish.multicast_publisher import MulticastPublisher
from tmp.subscribe.multicast_subscriber import MulticastSubscriber
# Python
import asyncio

loop = asyncio.get_event_loop()


class Node:

    def __init__(self):

        self.localSub = LocalSubscriber(5553)
        self.localSub.subscribe()

        self.multicastSub = MulticastSubscriber(MulticastGroup('239.1.1.1', 5554))
        self.multicastSub.subscribe()

        self.multicastPub = MulticastPublisher('192.168.8.100', MulticastGroup('239.1.1.1', 5555))
        self.multicastPub.connect()


    async def startLocal(self):

        while True:
            local = await self.localSub.process()
            await self.handlePackage(local)


    async def startMulticast(self):

        while True:
            remote = await self.localSub.process()
            await self.handlePackage(remote)


    async def handlePackage(self, package):
        print('send to multicast', package)
        await self.multicastPub.send(package)


if __name__ == '__main__':

    node =  Node()

    try:

        task1 = asyncio.ensure_future(node.startLocal())
        task2 = asyncio.ensure_future(node.startMulticast())

        loop.run_forever()

    finally:
        loop.close()

