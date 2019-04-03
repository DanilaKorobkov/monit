from monit.domain.observers.observer import *
# Internal
from monit.common.decorators import override
from monit.data_source.network_node import NetworkNode
# Python
import platform
import subprocess


class PingNodeObserver(Observer):

    def __init__(self, observeType, observeObject, interval, receiver, observedNetworkNode):
        super().__init__(observeType, observeObject, interval, receiver)

        self.observedNetworkNode = observedNetworkNode

    @override
    def process(self):

        status = self.__ping(self.observedNetworkNode.ip)
        status = {'status': status}
        return status


    @staticmethod
    def __ping(host):

        param = '-n' if platform.system() == 'Windows' else '-c'

        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0




observer = PingNodeObserver(observeType = 'other',
                            observeObject = 'server/network_connection',
                            interval = 5,
                            receiver = NetworkNode('127.0.0.1', 7000),
                            observedNetworkNode = NetworkNode('google.com'))
observer.observe()