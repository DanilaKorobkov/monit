# Internal
from monit.domain.observers.observer_factory import ObserverFactory
# Python
import yaml
from argparse import ArgumentParser


class ObserverApplicationController:

    def __init__(self):

        parser = ArgumentParser()
        parser.add_argument('--config', type = str)
        args = parser.parse_args().__dict__

        with open(args.get('config')) as observerConfig:

            config = yaml.load(observerConfig, Loader = yaml.FullLoader)

            self.observer = ObserverFactory().createObserver(config)
            self.observer.observe()


controller = ObserverApplicationController()