from tmp.subscribe.i_subscriber import *
# Internal
from monit.common.decorators import override
# Python
import zmq


class RequestReplySubscriber(ISubscriber):

    def __init__(self, port, packageCodingStrategy):
        super().__init__(packageCodingStrategy)

        self._port = port


    @override
    def process(self):

        self._subscribe()

        while True:

            data = self._socket.recv()
            package = self._packageCodingStrategy.decode(data)

            print(package)

            self._socket.send(self._packageCodingStrategy.encode({'status': 'ok'}))

            yield package


    @override
    def _subscribe(self):

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)
        self._socket.bind("tcp://*:{}".format(self._port))


if __name__ == '__main__':

    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy


    s1 = RequestReplySubscriber(port = 5554,
                                packageCodingStrategy = BsonCodingStrategy())
    iterObject = iter(s1.process())

    while True:
        next(iterObject)
