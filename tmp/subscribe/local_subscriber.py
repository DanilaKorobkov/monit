from tmp.subscribe.i_subscriber import *
# Internal
from monit.common.decorators import override
# Python
import zmq, zmq.asyncio


class LocalSubscriber(ISubscriber):

    def __init__(self, port):
        super().__init__()

        self._port = port


    @override
    def subscribe(self):

        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.SUB)

        self._socket.bind("tcp://*:{}".format(self._port))

        self._socket.setsockopt(zmq.SUBSCRIBE, b'')


    @override
    async def process(self):

        while True:

            data = await self._socket.recv()

            package = self._packageCodingStrategy.decode(data)
            return package



if __name__ == '__main__':

    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    s1 = LocalSubscriber(port = 5554)

    iterObject = iter(s1.process())

    while True:
        next(iterObject)
