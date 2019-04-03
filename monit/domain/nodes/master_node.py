from .node import *


class MasterNode(Node):

    def handleResult(self, result):
        raise NotImplementedError