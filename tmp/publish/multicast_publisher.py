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



if __name__ == '__main__':

    from tmp.multicast_group import MulticastGroup
    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    import time

    p1 = MulticastPublisher(networkCardIp = '192.168.1.1',
                            multicastGroup = MulticastGroup('239.1.1.1', 5555))
    p1.connect()


    while True:

        time.sleep(5)
        p1.send({'data': b'ok'})
