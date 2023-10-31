import json


class Config:

    def __init__(self, path):
        with open(path, 'r', encoding="utf8") as file:
            self.data = json.loads(file.read())

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            return self.data[item]

        ret = self.data
        for key in list(item):
            ret = ret[key]
        return ret
