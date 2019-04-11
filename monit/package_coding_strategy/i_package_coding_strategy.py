

class IPackageCodingStrategy:

    def encode(self, package):
        raise NotImplementedError

    def decode(self, package):
        raise NotImplementedError