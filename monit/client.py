# Python
import zmq
import bson


class Client:

    def __init__(self):

        self.socket = None
        self.context = None


    def connect(self, receiver):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://{}:{}".format(receiver.ip, receiver.port))


    def send(self, data):

        self.socket.send(data)
        return bson.loads(self.socket.recv())
