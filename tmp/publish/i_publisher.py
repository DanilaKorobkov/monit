# Internal
from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

class IPublisher:

    def __init__(self):

        self._context = None
        self._socket = None

        self._packageCodingStrategy = BsonCodingStrategy()


    def connect(self):
        raise NotImplementedError


    async def send(self, package):
        raise NotImplementedError

