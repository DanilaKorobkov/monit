

class ISubscriber:

    def __init__(self, packageCodingStrategy):

        self._context = None
        self._socket = None

        self._packageCodingStrategy = packageCodingStrategy


    def process(self):
        raise NotImplementedError


    def _subscribe(self):
        raise NotImplementedError
