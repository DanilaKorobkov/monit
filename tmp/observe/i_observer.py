from tmp.publish.local_publisher import *
# Python
import asyncio


class IObserver(LocalPublisher):

    def __init__(self, subject, interval, port):
        super().__init__(port)

        self._subject = subject
        self._interval = interval


    async def start(self):

        self.connect()

        while True:

            result = \
            {
                'subject': self._subject.getDictPresentation(),
                'result': self._process()
            }
            await self.send(result)

            print('send', result)
            await asyncio.sleep(self._interval)


    def _process(self):
        raise NotImplementedError
