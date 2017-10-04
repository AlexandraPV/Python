class Seance:
    def __init__(self, name, time, cinema):
        self.name = name
        self.time = time
        self.cinema = cinema

    def __str__(self):
        return 'name: %s, Time: %s, Cinema (name): %s' \
               % (self.name, self.time or '-', self.cinema or '-')