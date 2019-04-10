from .i_subscriber import *
# Internal
from monit.common.decorators import override
# Python
import zmq


class PublishSubscriber(ISubscriber):

    def __init__(self, multicastGroup, packageCodingStrategy):
        super().__init__(packageCodingStrategy)

        self._multicastGroup = multicastGroup


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

        self._socket.connect("epgm://{}:{}".format(self._multicastGroup.ip,
                                                   self._multicastGroup.port))

        self._socket.setsockopt(zmq.SUBSCRIBE, b'')



if __name__ == '__main__':

    from tmp.multicast_group import MulticastGroup
    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    s1 = PublishSubscriber(multicastGroup = MulticastGroup('239.1.1.1', 5555),
                           packageCodingStrategy = BsonCodingStrategy())

    iterObject = iter(s1.process())

    while True:
        next(iterObject)
