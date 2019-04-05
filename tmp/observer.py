# Internal
from tmp.publisher import Publisher
from monit.data_source.network_node import NetworkNode
# Python
import time
import bson


class Observer(Publisher):

    def __init__(self, interval, receiver: NetworkNode):
        super().__init__()

        self.interval = interval

        self.receiver = receiver


    def start(self):

        self.connect(self.receiver.ip, self.receiver.port)

        while True:

            result = \
            {
                'observeResult': self.process()
            }

            self.send(bson.dumps(result))

            time.sleep(self.interval)


    def process(self):
        raise NotImplementedError
