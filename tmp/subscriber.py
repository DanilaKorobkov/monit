# Internal
from tmp.multicast_group import MulticastGroup
# Python
import zmq


class Subscriber:

    def __init__(self):

        self.context = None
        self.socket = None


    def subscribe(self, multicastGroup):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        self.socket.connect("epgm://{}:{}".format(multicastGroup.ip, multicastGroup.port))

        self.socket.setsockopt(zmq.SUBSCRIBE, b'')


    def waitPackage(self):

        while True:

            package = self.socket.recv()
            print(package)
            yield package


if __name__ == '__main__':

    s1 = Subscriber()
    s1.subscribe(MulticastGroup('239.1.1.1', 5555))

    iterObject = iter(s1.waitPackage())

    while True:
        next(iterObject)
