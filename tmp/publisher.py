# Internal
from tmp.multicast_group import MulticastGroup
from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy
# Python
import zmq


class Publisher:

    def __init__(self, networkCardIp, multicastGroup, packageCodingStrategy):

        self.__context = None
        self.__socket = None

        self.__networkCardIp = networkCardIp
        self.__multicastGroup = multicastGroup

        self.__packageCodingStrategy = packageCodingStrategy


    def connect(self):

        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.PUB)

        self.__socket.connect("epgm://{};{}:{}".format(self.__networkCardIp,
                                                     self.__multicastGroup.ip,
                                                     self.__multicastGroup.port))


    def send(self, package):

        data = self.__packageCodingStrategy.encode(package)
        self.__socket.send(data)


if __name__ == '__main__':

    import time

    p1 = Publisher(networkCardIp = '192.168.1.1',
                   multicastGroup = MulticastGroup('239.1.1.1', 5555),
                   packageCodingStrategy = BsonCodingStrategy())
    p1.connect()


    while True:

        time.sleep(5)
        p1.send({'data': b'ok'})
