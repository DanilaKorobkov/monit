from tmp.publish.local_publisher import *
# Python
import time


class IObserver(LocalPublisher):

    def __init__(self, subject, interval, port):
        super().__init__(port)

        self._subject = subject
        self._interval = interval


    def start(self):

        self.connect()

        while True:

            result = \
            {
                'subject': self._subject.getDictPresentation(),
                'result': self._process()
            }
            self.send(result)

            time.sleep(self._interval)


    def _process(self):
        raise NotImplementedError
