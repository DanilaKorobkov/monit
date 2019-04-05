# Python
import zmq


class Subscriber:

    def __init__(self):

        self.context = None
        self.socket = None

    def connect(self, ip, port):

        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("epgm://239.1.1.1:5555")
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')


    def waitPackage(self):

        while True:

            package = self.socket.recv()
            print(package)
            yield package


if __name__ == '__main__':

    s1 = Subscriber()
    s1.connect('224.0.1.1', 5555)

    iterObject = iter(s1.waitPackage())

    while True:
        next(iterObject)
