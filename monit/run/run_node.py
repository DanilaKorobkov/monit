from monit.factories.node_factory import NodeFactory
# Python
import yaml
import asyncio
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type = str, help = 'Path to config file')

    args = parser.parse_args().__dict__

    with open(args.get('config'), 'r') as configFile:
        config = yaml.load(configFile)

    node = NodeFactory.createNode(config)

    try:
        tasks = asyncio.gather(node.processLocal(), node.processRemote())
        asyncio.get_event_loop().run_until_complete(tasks)

    finally:
        asyncio.get_event_loop().close()





