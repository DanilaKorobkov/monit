from monit.observe.base_input_device_observer import *


class MouseConnectionObserver(BaseInputDeviceObserver):

    def __init__(self, path, interval, port):
        super().__init__(path, interval, port, 'Mouse')
