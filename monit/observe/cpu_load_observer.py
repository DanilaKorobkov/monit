from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# 3rdparty
import psutil


class CPULoadObserver(IObserver):

    def __init__(self, path, interval, port, criticalThresholdPercent):
        super().__init__(path, interval, port)

        self._criticalThresholdPercent = criticalThresholdPercent


    @override
    def _process(self):

        return True if (psutil.cpu_percent() <= self._criticalThresholdPercent) else False
