

class IPublisher:

    def __init__(self, packageCodingStrategy):

        self._context = None
        self._socket = None

        self._packageCodingStrategy = packageCodingStrategy


    def connect(self):
        raise NotImplementedError


    def send(self, package):
        raise NotImplementedError

