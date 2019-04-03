# Internal
from monit.domain.nodes.node_factory import NodeFactory
# Python
import yaml


class NodeApplicationController:

    def __init__(self):

        with yaml.load('/home/user/Data/Other/Projects/monit/node.conf') as nodeConfig:

            self.node = NodeFactory().createNodeUsing(nodeConfig)
            self.node.start()
