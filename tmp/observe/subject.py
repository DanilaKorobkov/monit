

class Subject:

    def __init__(self, path):

        self._path = path


    def getDictPresentation(self):

        return \
        {
            'path': self._path
        }
