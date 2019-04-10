from tmp.publish.i_publisher import *
# Internal
from monit.common.decorators import override
# Python
import zmq


class LocalPublisher(IPublisher):

    def __init__(self, port, packageCodingStrategy):
        super().__init__(packageCodingStrategy)

        self._port = port


    @override
    def connect(self):

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB)

        self._socket.connect("tcp://127.0.0.1:{}".format(self._port))


    @override
    def send(self, package):

        data = self._packageCodingStrategy.encode(package)
        self._socket.send(data)



if __name__ == '__main__':

    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    import time

    p1 = LocalPublisher(port = 5554,
                        packageCodingStrategy = BsonCodingStrategy())
    p1.connect()


    while True:

        time.sleep(2)
        p1.send({'data': b'ok'})