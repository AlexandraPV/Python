from cinemas import Cinemas
from cinema import Cinema
from seances import Seances
from seance import Seance

import pickle



class Command:
    def __init__(self):
        self.cinemas = Cinemas('cinemas')
        self.seances = Seances('seances')

    @staticmethod
    def show_options():
        print('1 - Cinemas')
        print('2 - Seances')

    @staticmethod
    def ask(question):
        while True:
            check = input(question + ' (yes/no) ').lower()
            if check == 'yes':
                return True
            elif check == 'no':
                return False

    def serialize(self):
        try:
            self.cinemas.serialize()
            self.seances.serialize()
        except OSError as e:
            print(e)
        except pickle.PickleError:
            print('Serialization error!')

    def deserialize(self):
        try:
            self.cinemas.deserialize()
            self.seances.deserialize()
        except OSError as e:
            print(e)
        except pickle.PickleError:
            print('Deserialization error!')

    # Print:
    @staticmethod
    def print_help():

        print('print  -- Print list')
        print('add    -- Add item to list')
        print('edit   -- Edit list item')
        print('delete -- Remove item from list')
        print('filt -- Filter')
        print('help   -- Print all commands')
        print('exit   -- Exiting the program')

    def print_cinemas(self):
        print('Cinemas:')
        print(self.cinemas)

    def print_seances(self):
        print('Seances:')
        print(self.seances)

    # Add
    def add_cinema(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        if self.cinemas.exists(name):
            print('cinema already exists!')
            return
        city = input('City: ')
        seats = input('Seats: ')

        cinema = Cinema(name, city, seats)

        if cinema:
            self.cinemas.insert(cinema)
            print('Added:', cinema)


    def add_seance(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        if self.seances.exists(name):
            print('seance already exists!')
            return
        time = input('Time: ')
        cinema = input('cinema: ')
        if not self.cinemas.exists(cinema):
            print('cinema does not exist!')
            return

        seance = Seance(name, time, cinema)

        if seance:
            self.seances.insert(seance)
            print('Added:', seance)


    # Edit
    def edit_cinema(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        if not self.cinemas.exists(name):
            print('cinema does not exist!')
            return

        city = input('New city: ')
        seats = input('New seats: ')

        updated = self.cinemas.update(name, city, seats)
        print('Edited:', updated)

    def edit_seance(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        if not self.seances.exists(name):
            print('seance does not exist!')
            return

        time = input('New time: ')
        cinema = input('New cinema: ')
        if not self.cinemas.exists(cinema):
            print('cinema does not exist!')
            return

        updated = self.seances.update(name, time, cinema)
        print('Edited:', updated)

    # Delete
    def delete_cinema(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        check = self.cinemas.remove(name)
        if check:
            self.seances.delete_cinemas(name)
            print('Successfully deleted!')
        else:
            print('cinema does not exist!')

    def delete_seance(self):
        name = input('name: ')
        if not name:
            print('Invalid input!')
            return
        check = self.seances.remove(name)
        if check:
            print('Successfully deleted!')
        else:
            print('seance does not exist!')


    # Search
    def search_cinemas(self):
        time = input('Time: ')
        if not time:
            print('Invalid input!')
            return
        names = self.seances.get_cinemas(lambda x: x.time >= time)
        filtered = self.cinemas.filter(lambda x: x.name in names)
        print('Filtered by time:', time)
        print('\n'.join(str(x) for x in filtered))