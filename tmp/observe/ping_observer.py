from tmp.observe.i_observer import *
# Internal
from monit.common.decorators import override
# Python
import platform
import subprocess


class PingNodeObserver(IObserver):

    def __init__(self, subject, interval, port, packageCodingStrategy, observedIp):
        super().__init__(subject, interval, port, packageCodingStrategy)

        self._observedIp = observedIp


    @override
    def process(self):

        status = self.__ping(self._observedIp)
        return status


    @staticmethod
    def __ping(host):

        param = '-n' if platform.system() == 'Windows' else '-c'

        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0




if __name__ == '__main__':

    from tmp.observe.subject import Subject
    from tmp.package_coding_strategy.bson_coding_strategy import BsonCodingStrategy

    observer = PingNodeObserver(subject = Subject(path = '/network/ping/client1'),
                                interval = 5,
                                port = 5554,
                                packageCodingStrategy = BsonCodingStrategy(),
                                observedIp = 'google.com')
    observer.start()