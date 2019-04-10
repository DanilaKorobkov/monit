from tmp.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import os

# TODO: Config: criticalThreshold

class DiskSpaceObserver(IObserver):

    def __init__(self, subject, interval, port, criticalThresholdPercent):
        super().__init__(subject, interval, port)

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

    from tmp.observe.subject import Subject
    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy
    import asyncio



    observer = DiskSpaceObserver(subject = Subject(path = '/os/disk/space'),
                                 interval = 5,
                                 port = 5553,
                                 criticalThresholdPercent = 70)

    asyncio.ensure_future(observer.start())
    asyncio.get_event_loop().run_forever()