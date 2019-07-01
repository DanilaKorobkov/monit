from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import re, subprocess


class BaseInputDeviceObserver(IObserver):


    def __init__(self, path, interval, port, deviceName):
        super().__init__(path, interval, port)

        self.deviceName = deviceName


    @override
    def _process(self):

        devices = subprocess.check_output('cat /proc/bus/input/devices', shell = True).decode('utf-8')

        keyboards = re.findall(r'({}=")(\w|\s)*(Keyboard)(")'.format(self.deviceName), devices)
        return bool(keyboards)
