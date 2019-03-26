"""Количество свободного места на разделе, где находится указанная папка"""

from src.domain.disk_space_observer.i_observer import *
# Python
import os


class DiskSpaceObserver(IObserver):

    criticalThreshold = 0.1

    @classmethod
    def check(cls):

        statvfs = os.statvfs("/")

        size = cls.fromBToGb(statvfs.f_frsize * statvfs.f_blocks)
        free = cls.fromBToGb(statvfs.f_frsize * statvfs.f_bavail)

        return True if (free / size >= cls.criticalThreshold) else False


    @staticmethod
    def fromBToGb(value):

        return value / (1024 ** 3)