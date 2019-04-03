from monit.data_source.zmq.server import *
# Python


class Node(Server):

    def __init__(self, port, whoami):
        super().__init__(port)

        self.whoami = whoami


    def work(self):

        iterObject = iter(self.start())

        while True:

            result = next(iterObject)
            result.update({'path': self.whoami + '/' + result.get('path')})

            print(result)

            self.handleResult(result)


    def handleResult(self, result):
        raise NotImplementedError

