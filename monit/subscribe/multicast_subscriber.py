from .i_subscriber import *
# Internal
from monit.common.decorators import override
# Python
import zmq, zmq.asyncio


class MulticastSubscriber(ISubscriber):

    def __init__(self, multicastGroup):
        super().__init__()

        self._multicastGroup = multicastGroup


    @override
    def subscribe(self):

        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.SUB)

        self._socket.connect("epgm://{}:{}".format(self._multicastGroup.ip,
                                                   self._multicastGroup.port))
        self._socket.setsockopt(zmq.SUBSCRIBE, b'')


    @override
    async def process(self):

        data = await self._socket.recv()

        package = self._packageCodingStrategy.decode(data)
        return package
