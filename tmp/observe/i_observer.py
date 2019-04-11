from tmp.publish.local_publisher import *
# Python
import asyncio


class IObserver(LocalPublisher):

    def __init__(self, path, interval, port):
        super().__init__(port)

        self._path = path
        self._interval = interval


    async def start(self):

        self.connect()

        while True:

            result = {'path': self._path, 'state': self._process()}
            await self.send(result)

            print('send', result)
            await asyncio.sleep(self._interval)


    def _process(self):
        raise NotImplementedError
