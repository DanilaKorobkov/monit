from monit.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import platform
import subprocess


class LinkObserver(IObserver):

    def __init__(self, path, interval, port, observedIp):
        super().__init__(path, interval, port)

        self._observedIp = observedIp


    @override
    def _process(self):

        status = self.__ping(self._observedIp)
        return status


    @staticmethod
    def __ping(host):

        param = '-n' if platform.system() == 'Windows' else '-c'

        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0




if __name__ == '__main__':

    observer = LinkObserver(path = '/network/ping/client1',
                            interval = 5,
                            port = 1111,
                            observedIp = 'google.com')

    asyncio.ensure_future(observer.start())
    asyncio.get_event_loop().run_forever()