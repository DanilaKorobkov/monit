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

        data = await self._socket.recv()

        package = self._packageCodingStrategy.decode(data)
        return package
