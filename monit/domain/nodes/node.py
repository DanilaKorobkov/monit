from monit.data_source.zmq.server import *
# Python


class Node(Server):

    def __init__(self, name, port):
        super().__init__(port)

        self.name = name


    def work(self):

        iterObject = iter(self.start())

        while True:

            result = next(iterObject)
            result.update({'path': self.name + '/' + result.get('path')})

            print(result)

            self.handleResult(result)


    def handleResult(self, result):
        raise NotImplementedError

