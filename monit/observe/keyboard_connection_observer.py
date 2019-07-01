from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import re, subprocess


class KeyboardConnectionObserver(IObserver):

    @override
    def _process(self):

        devices = subprocess.check_output('cat /proc/bus/input/devices', shell = True).decode('utf-8')

        keyboards = re.findall(r'(Name=")(\w|\s)*(Keyboard)(")', devices)
        return bool(keyboards)
