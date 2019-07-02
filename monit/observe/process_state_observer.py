from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import subprocess


class ProcessStateObserver(IObserver):

    def __init__(self, path, interval, port, processName):
        super().__init__(path, interval, port)

        self.processName = processName


    @override
    def _process(self):

        isProcessActive = subprocess.call('ps -A | grep {}'.format(self.processName), shell = True)
        return isProcessActive == 0
