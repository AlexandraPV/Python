from command import Command


def main():

    command = Command()
    command.deserialize()


    while True:
        str = input('Enter command: ').strip().lower()

        if str == 'help':
            Command.print_help()

        elif str == 'exit':
            break

        elif str == 'print':
            Command.show_options()
            print('3 - All')

            num = input('?: ')
            if num == '1':
                command.print_cinemas()
            elif num == '2':
                command.print_seances()
            elif num == '3':
                command.print_cinemas()
                command.print_seances()
            else:
                print('Invalid input!')

        elif str == 'add':
            Command.show_options()

            num = input('?: ')
            if num == '1':
                command.add_cinema()
            elif num == '2':
                command.add_seance()
            else:
                print('Invalid input!')

        elif str == 'edit':
            Command.show_options()

            num = input('?: ')
            if num == '1':
                command.edit_cinema()
            elif num == '2':
                command.edit_seance()
            else:
                print('Invalid input!')

        elif str == 'delete':
            Command.show_options()

            num = input('?: ')
            if num == '1':
                command.delete_cinema()
            elif num == '2':
                command.delete_seance()
            else:
                print('Invalid input!')


        elif str == 'filt':
            command.search_cinemas()

    command.serialize()


if __name__ == "__main__":
    main()