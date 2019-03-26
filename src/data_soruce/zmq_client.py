# Python
import zmq
import bson


class ZmqClient:

    url = 'tcp://127.0.0.1:7000'

    def __init__(self):

        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(self.url)


    def __del__(self):

        self.context.destroy()


    def send(self, status):

        package = {'status': status}

        self.socket.send(bson.dumps(package))
        return bson.loads(self.socket.recv())


