from tmp.subscribe.i_subscriber import *
# Internal
from monit.common.decorators import override
# Python
import zmq


class LocalSubscriber(ISubscriber):

    def __init__(self, port):
        super().__init__()

        self._port = port


    @override
    def process(self):

        self._subscribe()

        while True:

            data = self._socket.recv()
            package = self._packageCodingStrategy.decode(data)

            print(package)
            yield package


    @override
    def _subscribe(self):

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)

        self._socket.bind("tcp://*:{}".format(self._port))

        self._socket.setsockopt(zmq.SUBSCRIBE, b'')



if __name__ == '__main__':

    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    s1 = LocalSubscriber(port = 5554)

    iterObject = iter(s1.process())

    while True:
        next(iterObject)
