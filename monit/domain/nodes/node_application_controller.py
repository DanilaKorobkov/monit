# Internal
from monit.domain.nodes.node_factory import NodeFactory
# Python
import yaml
from argparse import ArgumentParser


class NodeApplicationController:

    def __init__(self):

        parser = ArgumentParser()
        parser.add_argument('--config', type = str)
        args = parser.parse_args().__dict__

        with open(args.get('config')) as nodeConfig:

            config = yaml.load(nodeConfig, Loader = yaml.FullLoader)

            self.node = NodeFactory().createNodeUsing(config)
            self.node.work()


a = NodeApplicationController()