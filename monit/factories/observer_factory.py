# Internal
from monit.observe.link_observer import LinkObserver
from monit.observe.disk_space_observer import DiskSpaceObserver
from monit.observe.mouse_connection_observer import MouseConnectionObserver
from monit.observe.keyboard_connection_observer import KeyboardConnectionObserver


class ObserverFactory:

    @classmethod
    def createObserver(cls, config):

        observerType = config.get('type')

        creators = \
        {
            'link': cls.createLinkObserver,
            'disk_space': cls.createDiskSpaceObserver,
            'mouse_connection': cls.createMouseConnectionObserver,
            'keyboard_connection': cls.createKeyboardConnectionObserver,
        }

        if observerType in creators:
            return creators.get(observerType)(config.get('observer')) if observerType in creators else None



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


    @staticmethod
    def createMouseConnectionObserver(config):

        return MouseConnectionObserver(path = config.get('path'),
                                       interval = config.get('interval'),
                                       port = config.get('localPublisherPort'))


    @staticmethod
    def createKeyboardConnectionObserver(config):

        return KeyboardConnectionObserver(path = config.get('path'),
                                          interval = config.get('interval'),
                                          port = config.get('localPublisherPort'))
