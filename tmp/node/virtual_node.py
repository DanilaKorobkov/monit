# Internal
from tmp.multicast_group import MulticastGroup
from tmp.subscribe.local_subscriber import LocalSubscriber
from tmp.publish.multicast_publisher import MulticastPublisher
from tmp.subscribe.multicast_subscriber import MulticastSubscriber
# Python
import asyncio

loop = asyncio.get_event_loop()


class VirtualNode:

    def __init__(self, name, port):

        self._name = name

        self.localSub = LocalSubscriber(port)
        self.localSub.subscribe()


        self.multicastPub = MulticastPublisher('10.13.0.171', MulticastGroup('239.1.1.1', 5554))
        self.multicastPub.connect()


    async def processLocal(self):

        while True:
            local = await self.localSub.process()
            await self.handlePackage(local)


    async def handlePackage(self, package):

        package['path'] = '/' + self._name + package['path']
        await self.multicastPub.send(package)
        print('self.multicastPub.send', package)


if __name__ == '__main__':

    node =  VirtualNode('prima', 5552)

    try:
        task1 = asyncio.ensure_future(node.processLocal())
        loop.run_forever()

    finally:
        loop.close()

