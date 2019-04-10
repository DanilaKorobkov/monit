# Internal
from tmp.multicast_group import MulticastGroup
# Python
import zmq


class Publisher:

    def __init__(self):

        self.context = None
        self.socket = None


    def connect(self, networkCardIp, multicastGroup):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.connect("epgm://{};{}:{}".format(networkCardIp, multicastGroup.ip, multicastGroup.port))


    def send(self, data):
        self.socket.send(data)


if __name__ == '__main__':

    import time

    p1 = Publisher()
    p1.connect(networkCardIp = '192.168.1.1',
               multicastGroup = MulticastGroup('239.1.1.1', 5555))


    while True:

        time.sleep(5)
        p1.send(b'DDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
