from .i_package_coding_strategy import *
# Python
import bson


class BsonCodingStrategy(IPackageCodingStrategy):

    def encode(self, package):

        return bson.dumps(package)


    def decode(self, package):

        return bson.loads(package)
