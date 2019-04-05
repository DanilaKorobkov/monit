import zmq


class Proxy:

    def __init__(self):

        self.context = None

        self.xPubSocket = None
        self.xSubSocket = None


    def proxyBetween(self, subPort, pubPort):

        self.context = zmq.Context()

        self.xSubSocket = self.context.socket(zmq.XSUB)
        self.xSubSocket.bind("tcp://*:{}".format(subPort))

        self.xPubSocket = self.context.socket(zmq.XPUB)
        self.xPubSocket.bind("tcp://*:{}".format(pubPort))

        zmq.proxy(self.xSubSocket, self.xPubSocket)


if __name__ == '__main__':

    proxy = Proxy()
    proxy.proxyBetween(6000, 6001)