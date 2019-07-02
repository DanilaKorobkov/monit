# Internal
from monit.observe.link_observer import LinkObserver
from monit.observe.cpu_load_observer import CPULoadObserver
from monit.observe.disk_space_observer import DiskSpaceObserver
from monit.observe.process_state_observer import ProcessStateObserver
from monit.observe.mouse_connection_observer import MouseConnectionObserver
from monit.observe.keyboard_connection_observer import KeyboardConnectionObserver
# Python
import os


class ObserverFactory:

    @classmethod
    def createObserver(cls, config):

        observerType = config.get('type')

        creators = \
        {
            'link': cls.createLinkObserver,
            'cpu_load': cls.createCPULoadObserver,
            'disk_space': cls.createDiskSpaceObserver,
            'process_state': cls.createProcessStateObserver,
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
    def createCPULoadObserver(config):

        return CPULoadObserver(path = config.get('path'),
                               interval = config.get('interval'),
                               port = config.get('localPublisherPort'),
                               criticalThresholdPercent = config.get('criticalThresholdPercent'))


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
    def createProcessStateObserver(config):

        return ProcessStateObserver(path = os.path.join(config.get('path'), config.get('processName')),
                                    interval = config.get('interval'),
                                    port = config.get('localPublisherPort'),
                                    processName = config.get('processName'))


    @staticmethod
    def createKeyboardConnectionObserver(config):

        return KeyboardConnectionObserver(path = config.get('path'),
                                          interval = config.get('interval'),
                                          port = config.get('localPublisherPort'))
