from tmp.subscribe.local_subscriber import *
from tmp.subscribe.multicast_subscriber import *
# Tmp
from tmp.multicast_group import MulticastGroup
from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy


class Node:

    def __init__(self):

        self.localSub = LocalSubscriber(5554, BsonCodingStrategy())
        self.multicastSub = MulticastSubscriber(MulticastGroup('239.1.1.1', 5555), BsonCodingStrategy())
