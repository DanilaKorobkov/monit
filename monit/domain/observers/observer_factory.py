# Internal
from monit.data_source.network_node import NetworkNode
from monit.domain.observers.ping_node_observer import PingNodeObserver
from monit.domain.observers.disk_space_observer import DiskSpaceObserver


class ObserverFactory:

    @classmethod
    def createObserver(cls, config):

        observerType = config.get('type')

        if observerType == 'disk_space':
            return cls.createDiskSpaceObserver(config.get('observer'))

        if observerType == 'ping_node':
            return cls.createPingNodeObserver(config.get('observer'))


    @staticmethod
    def createDiskSpaceObserver(observer):

        return DiskSpaceObserver(observeType = observer.get('type'),
                                 observeObject = observer.get('object'),
                                 interval = observer.get('interval'),
                                 criticalThresholdPercent = observer.get('criticalThresholdPercent'),
                                 receiver = NetworkNode(observer.get('receiver').get('ip'),
                                                        observer.get('receiver').get('port')))

    @staticmethod
    def createPingNodeObserver(observer):

        return PingNodeObserver(observeType = observer.get('type'),
                                observeObject = observer.get('object'),
                                interval = observer.get('interval'),
                                observedNetworkNode = NetworkNode(observer.get('observed').get('ip')),
                                receiver = NetworkNode(observer.get('receiver').get('ip'),
                                                       observer.get('receiver').get('port')))