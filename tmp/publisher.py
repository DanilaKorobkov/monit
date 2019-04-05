# Python
import zmq


class Publisher:

    def __init__(self):

        self.context = None
        self.socket = None

    def connect(self, ip, port):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://*:5555")


    def send(self, data):

        self.socket.send(data)


if __name__ == '__main__':

    import time

    p1 = Publisher()
    p1.connect('', 0)


    while True:

        time.sleep(5)
        p1.send(b'DDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
