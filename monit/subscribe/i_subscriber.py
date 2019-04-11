# Internal
from monit.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy


class ISubscriber:

    def __init__(self):

        self._context = None
        self._socket = None

        self._packageCodingStrategy = BsonCodingStrategy()


    def process(self):
        raise NotImplementedError


    def subscribe(self):
        raise NotImplementedError
