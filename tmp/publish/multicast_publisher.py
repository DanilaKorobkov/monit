from .i_publisher import *
# Internal
from monit.common.decorators import override
# Python
import zmq, zmq.asyncio


class MulticastPublisher(IPublisher):

    def __init__(self, networkCardIp, multicastGroup):
        super().__init__()

        self._networkCardIp = networkCardIp
        self._multicastGroup = multicastGroup


    @override
    def connect(self):

        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.PUB)

        self._socket.connect("epgm://{};{}:{}".format(self._networkCardIp,
                                                      self._multicastGroup.ip,
                                                      self._multicastGroup.port))

    @override
    async def send(self, package):

        data = self._packageCodingStrategy.encode(package)
        await self._socket.send(data)
