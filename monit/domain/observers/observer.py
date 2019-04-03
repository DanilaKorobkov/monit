from MonitoringSystem.client import *
# Python
import bson
import time


class Observer(Client):

    def __init__(self, observeType, observeObject, interval, receiver):
        super().__init__()

        self.observeType = observeType
        self.observeObject = observeObject

        self.interval = interval

        self.receiver = receiver


    def observe(self):

        self.connect(self.receiver)

        while True:

            result = \
            {
                'path': self.__getPath(),
                'observeResult': self.process()
            }

            self.send(bson.dumps(result))

            time.sleep(self.interval)


    def process(self):
        raise NotImplementedError


    def __getPath(self):

        return '/'.join([self.observeType, self.observeObject])
