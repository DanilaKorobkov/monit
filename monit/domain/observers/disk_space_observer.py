from MonitoringSystem.observer import *
# Internal
from MonitoringSystem.network_node import NetworkNode
from MonitoringSystem.common.decorators import override
# Python
import os

# TODO: Config: criticalThreshold

class DiskSpaceObserver(Observer):

    def __init__(self, observeType, observeObject, interval, receiver, criticalThresholdPercent):
        super().__init__(observeType, observeObject, interval, receiver)

        self.criticalThresholdPercent = criticalThresholdPercent


    @override
    def process(self):

        statvfs = os.statvfs("/")

        size = self.__fromBToGb(statvfs.f_frsize * statvfs.f_blocks)
        free = self.__fromBToGb(statvfs.f_frsize * statvfs.f_bavail)

        status = True if (free / size * 100 >= self.criticalThresholdPercent) else False
        status = {'status': status}
        return status


    @staticmethod
    def __fromBToGb(value):

        return value / (1024 ** 3)


observer = DiskSpaceObserver(observeType = 'self',
                             observeObject = 'os/disk/space',
                             interval = 5,
                             receiver = NetworkNode('127.0.0.1', 7000),
                             criticalThresholdPercent = 10)
observer.observe()