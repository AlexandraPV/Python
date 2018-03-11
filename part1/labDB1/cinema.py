class Cinema:
    def __init__(self, name, city, seats):
        self.name = name
        self.city = city
        self.seats = seats

    def __str__(self):
        return 'name: %s, City: %s, Count of seats: %s' \
               % (self.name, self.city or '-', self.seats or '-')