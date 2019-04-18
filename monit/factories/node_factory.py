# Internal
from monit.node.node import Node
from monit.node.virtual_node import VirtualNode


class NodeFactory:

    @classmethod
    def createNode(cls, config):

        nodeType = config.get('type')

        if nodeType == 'basic':
            return cls.__createNode(config.get('node'))

        if nodeType == 'virtual':
            return cls.__createVirtualNode(config.get('node'))


    @staticmethod
    def __createNode(config):

        return Node(name = config.get('name'),
                    localSubsPort = config.get('localSubsPort'),
                    multicastGroupIp = config.get('multicastGroupIp'),
                    multicastGroupPort = config.get('multicastGroupPort'),
                    ownIp = config.get('ownIp'),
                    localPublishPort = config.get('localPublishPort'))


    @staticmethod
    def __createVirtualNode(config):

        return VirtualNode(name = config.get('name'),
                           localSubsPort = config.get('localSubsPort'),
                           multicastGroupIp = config.get('multicastGroupIp'),
                           multicastGroupPort = config.get('multicastGroupPort'),
                           ownIp = config.get('ownIp'),
                           localPublishPort = config.get('localPublishPort'))