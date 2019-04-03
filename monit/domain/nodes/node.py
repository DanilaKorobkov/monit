from monit.data_source.zmq.server import *
# Python


class Node(Server):

    def __init__(self, port, whoami):
        super().__init__(port)

        self.whoami = whoami


    def start_impl(self):

        iterObject = iter(self.start())

        while True:

            result = next(iterObject)

            result.update({'path': self.whoami + '/' + result.get('path')})
            print(result)



node = Node(port = 7000, whoami = 'client_1')
node.start_impl()