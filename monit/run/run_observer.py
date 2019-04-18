from monit.factories.observer_factory import ObserverFactory
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

    observer = ObserverFactory.createObserver(config)

    try:
        asyncio.get_event_loop().run_until_complete(observer.start())

    finally:
        asyncio.get_event_loop().close()





