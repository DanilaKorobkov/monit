from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import os

# TODO: Config: criticalThreshold

class DiskSpaceObserver(IObserver):

    def __init__(self, path, interval, port, criticalThresholdPercent):
        super().__init__(path, interval, port)

        self._criticalThresholdPercent = criticalThresholdPercent


    @override
    def _process(self):

        statvfs = os.statvfs("/")

        size = self.__fromBToGb(statvfs.f_frsize * statvfs.f_blocks)
        free = self.__fromBToGb(statvfs.f_frsize * statvfs.f_bavail)

        return True if (free / size * 100 >= self._criticalThresholdPercent) else False


    @staticmethod
    def __fromBToGb(value):

        return value / (1024 ** 3)

if __name__ == '__main__':

    import asyncio



    observer = DiskSpaceObserver(path = '/os/disk/space',
                                 interval = 2,
                                 port = 1111,
                                 criticalThresholdPercent = 70)

    try:
        asyncio.get_event_loop().run_until_complete(observer.start())

    finally:
        asyncio.get_event_loop().close()