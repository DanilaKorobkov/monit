# Internal
from tmp.multicast_group import MulticastGroup
from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy
# Python
import zmq


class Subscriber:

    def __init__(self, multicastGroup, packageCodingStrategy):

        self.__context = None
        self.__socket = None

        self.__multicastGroup = multicastGroup

        self.__packageCodingStrategy = packageCodingStrategy


    def subscribe(self):

        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.SUB)

        self.__socket.connect("epgm://{}:{}".format(self.__multicastGroup.ip, self.__multicastGroup.port))

        self.__socket.setsockopt(zmq.SUBSCRIBE, b'')


    def waitPackage(self):

        while True:

            data = self.__socket.recv()
            package = self.__packageCodingStrategy.decode(data)

            print(package)
            yield package



if __name__ == '__main__':

    s1 = Subscriber(multicastGroup = MulticastGroup('239.1.1.1', 5555),
                    packageCodingStrategy = BsonCodingStrategy())
    s1.subscribe()

    iterObject = iter(s1.waitPackage())

    while True:
        next(iterObject)
