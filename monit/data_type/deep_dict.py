

class AvkDict:

    def __init__(self):

        self.dictionary = {'avk': {}}


    def deepUpdate(self, otherDict):

        return self._deepUpdateImpl(self.dictionary['avk'], otherDict)


    def get(self, key):
        return {key: self.dictionary.get('avk').get(key, None)}


    def __getattr__(self, item):
        return getattr(self.dictionary, item)


    def _deepUpdateImpl(self, ownDict, otherDict):

        ownKeys = set(ownDict.keys())
        otherKeys = set(otherDict.keys())

        needToAppend = otherKeys - ownKeys
        needToUpdate = otherKeys & ownKeys

        for key in needToAppend:
            ownDict.update({key: otherDict[key]})

        for key in needToUpdate:

            if type(otherDict[key]) is dict and type(ownDict[key]) is dict:
                self._deepUpdateImpl(ownDict[key], otherDict[key])

            else:
                ownDict[key] = otherDict[key]

    @staticmethod
    def convertPathToEmptyDict(path, value):

        path = path.split('/')[1:]

        result = value

        for key in reversed(path):
            result = {key: result}

        return result
