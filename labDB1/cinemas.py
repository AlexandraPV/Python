from collection import Collection


class Cinemas(Collection):
    def update(self, name, city, seats):
        updated = self.find(name)
        if updated:
            if city:
                updated.city = city
            if seats:
                updated.seats = seats
        return updated