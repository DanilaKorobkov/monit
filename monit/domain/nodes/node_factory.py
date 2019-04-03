# Internal
from monit.domain.nodes.slave_node import SlaveNode
from monit.domain.nodes.master_node import MasterNode
from monit.data_source.network_node import NetworkNode


class NodeFactory:

    @classmethod
    def createNodeUsing(cls, config):

        nodeType = config.get('type')

        if nodeType == 'master':
            return cls.createMasterNode(config.get('node'))

        if nodeType == 'slave':
            return cls.createSlaveNode(config.get('node'))


    @staticmethod
    def createMasterNode(nodeInfo):

        return MasterNode(name = nodeInfo.get('name'),
                          port = nodeInfo.get('port'))


    @staticmethod
    def createSlaveNode(nodeInfo):

        return SlaveNode(name = nodeInfo.get('name'),
                         port = nodeInfo.get('port'),
                         receiver = NetworkNode(ip = nodeInfo.get('receiver').get('ip'),
                                                port = nodeInfo.get('receiver').get('port')))