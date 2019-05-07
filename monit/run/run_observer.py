from monit.factories.observer_factory import ObserverFactory
# Python
import os
import yaml
import asyncio
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type = str, help = 'Path to config file')

    args = parser.parse_args().__dict__

    pathToConfigFile = args.get('config')

    with open(pathToConfigFile, 'r') as configFile:
        config = yaml.load(configFile)

    pathToNodeConfigFile = os.path.join(os.path.dirname(pathToConfigFile), '{}.conf'.format(config.get('observer').get('connectWith')))
    with open(pathToNodeConfigFile) as nodeConfigFile:

        nodeConfig = yaml.load(nodeConfigFile).get('node')
        config['observer']['localPublisherPort'] = nodeConfig.get('localSubsPort')


    observer = ObserverFactory.createObserver(config)

    try:
        asyncio.get_event_loop().run_until_complete(observer.start())

    finally:
        asyncio.get_event_loop().close()
