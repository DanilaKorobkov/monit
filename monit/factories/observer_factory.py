# Internal
from monit.observe.link_observer import LinkObserver
from monit.observe.disk_space_observer import DiskSpaceObserver


class ObserverFactory:

    @classmethod
    def createObserver(cls, config):

        observerType = config.get('type')

        if observerType == 'link':
            return cls.createLinkObserver(config.get('observer'))

        if observerType == 'disk_space':
            return cls.createDiskSpaceObserver(config.get('observer'))


    @staticmethod
    def createLinkObserver(config):

        return LinkObserver(path = config.get('path'),
                            interval = config.get('interval'),
                            port = config.get('localPublisherPort'),
                            observedIp = config.get('observedIp'))


    @staticmethod
    def createDiskSpaceObserver(config):

        return DiskSpaceObserver(path = config.get('path'),
                                 interval = config.get('interval'),
                                 port = config.get('localPublisherPort'),
                                 criticalThresholdPercent = config.get('criticalThresholdPercent'))
