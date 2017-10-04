import pickle


class Collection:
    def __init__(self, name):
        self.list = []
        self.name = name

    def exists(self, name):
        return any(x.name == name for x in self.list)

    def insert(self, item):
        if not self.exists(item.name):
            self.list.append(item)

    def find(self, name):
        return next((x for x in self.list if x.name == name), None)

    def names(self, check=lambda x: True):
        return [x.name for x in self.list if check(x)]

    def filter(self, check):
        return list(filter(check, self.list))

    def remove(self, name):
        x = self.find(name)
        if x:
            self.list.remove(x)
            return True
        return False

    def drop(self):
        del self.list[:]

    def serialize(self):
        with open(self.name, 'wb') as f:
            pickle.dump(self.list, f)

    def deserialize(self):
        with open(self.name, 'rb') as f:
            self.list = pickle.load(f)

    def __str__(self):
        return '\n'.join(str(x) for x in self.list)