from collection import Collection


class Seances(Collection):
    def update(self, name, time, cinema):
        updated = self.find(name)
        if updated:
            if time:
                updated.whence = time
            if cinema:
                updated.plane = cinema
        return updated

    def get_cinemas(self, check):
        return [x.cinema for x in self.list if check(x)]

    def delete_cinemas(self, *names):
        for x in self.list:
            if x.cinema in names:
                x.cinema = None