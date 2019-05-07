# Internal
from monit.node.node import Node


class NodeFactory:

    @classmethod
    def createNode(cls, config):

        return cls.__createNode(config.get('node'))


    @staticmethod
    def __createNode(config):

        return Node(name = config.get('name'),
                    localSubsPort = config.get('localSubsPort'),
                    multicastGroupIp = config.get('multicastGroupIp'),
                    multicastGroupPort = config.get('multicastGroupPort'),
                    ownIps = config.get('ownIps'),
                    localPublishPort = config.get('localPublishPort'))
