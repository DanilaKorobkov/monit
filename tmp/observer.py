from tmp.publisher import *
# Python
import time
import bson


class Observer(Publisher):

    def __init__(self, interval, networkCardIp, multicastGroup):
        super().__init__(networkCardIp, multicastGroup)

        self.interval = interval


    def start(self):

        self.connect()

        while True:

            result = \
            {
                'observeResult': self.process()
            }

            self.send(bson.dumps(result))

            time.sleep(self.interval)


    def process(self):
        raise NotImplementedError
