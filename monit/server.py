# Python
import zmq
import bson

class Server:

    def __init__(self, port):

        self.port = port

        self.socket = None
        self.context = None

    def start(self):

        self.__bind()

        while True:

            try:
                yield self.__process()

            except Exception as exception:
                self.__handleException(exception)


    def __bind(self):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:{port}".format(port = self.port))


    def __process(self):

        request = self.socket.recv()
        request = bson.loads(request)

        self.socket.send(bson.dumps({'status': 'ok'}))

        return request


    def __handleException(self, exception: Exception):

        reply = self.__wrapException(exception)
        reply = bson.dumps(reply)
        self.socket.send_multipart([reply])


    @staticmethod
    def __wrapException(exception: Exception):

        return {'error': {'exception': exception.__class__.__name__, 'description': str(exception)}}
