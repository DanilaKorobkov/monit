from tmp.publish.i_publisher import *
# Internal
from monit.common.decorators import override
# Python
import zmq
import zmq.asyncio


class LocalPublisher(IPublisher):

    def __init__(self, port):
        super().__init__()

        self._port = port


    @override
    def connect(self):

        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.PUB)

        self._socket.connect("tcp://127.0.0.1:{}".format(self._port))


    @override
    async def send(self, package):

        data = self._packageCodingStrategy.encode(package)
        await self._socket.send(data)



if __name__ == '__main__':

    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    import time

    p1 = LocalPublisher(port = 5554)
    p1.connect()


    while True:

        time.sleep(2)
        p1.send({'data': b'ok'})
