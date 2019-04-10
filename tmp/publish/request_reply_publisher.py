from tmp.publish.i_publisher import *
# Internal
from monit.common.decorators import override
# Python
import zmq


class RequestReplyPublisher(IPublisher):

    def __init__(self, networkNode, packageCodingStrategy):
        super().__init__(packageCodingStrategy)

        self._networkNode = networkNode


    @override
    def connect(self):
        
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)

        self._socket.connect("tcp://{}:{}".format(self._networkNode.ip,
                                                  self._networkNode.port))


    @override
    def send(self, package):
        
        data = self._packageCodingStrategy.encode(package)
        self._socket.send(data)
        
        answer = self._socket.recv()
        return self._packageCodingStrategy.decode(answer)



if __name__ == '__main__':

    from monit.data_source.network_node import NetworkNode
    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    import time


    p1 = RequestReplyPublisher(networkNode = NetworkNode('127.0.0.1', 5554),
                               packageCodingStrategy = BsonCodingStrategy())
    p1.connect()

    while True:

        time.sleep(5)
        p1.send({'data': b'ok'})
