from monit.domain.nodes.node import *
# Internal
from monit.common.decorators import override
from monit.data_source.zmq.client import Client
from monit.data_source.network_node import NetworkNode
# Python
import bson

class SlaveNode(Node):

    def __init__(self, port, whoami, receiver):
        super().__init__(port, whoami)

        self.receiver = receiver

        self.client = Client()


    def work(self):

        self.client.connect(self.receiver)

        Node.work(self)



    @override
    def handleResult(self, result):

        return self.client.send(bson.dumps(result))



node = SlaveNode(port = 7000, whoami = 'client_1', receiver = NetworkNode(ip = '127.0.0.1', port = 7777))
node.work()