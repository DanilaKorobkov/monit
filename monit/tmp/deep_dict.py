import collections


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



if __name__ == '__main__':

    a1 = {'client1': {'os': 1}}
    b = {'client2': {'os': 2}}

    a = AvkDict()
    a.deepUpdate(a1)

    a.deepUpdate(b)


    c = '/os/disk/space'
    c = c.split('/')[1: ]

    result = {}

    for key in reversed(c):
        result = {key: result}

    print(a.dictionary)