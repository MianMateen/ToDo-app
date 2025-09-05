from todo_class import ToDo
from test import GUi

if __name__ == '__main__':
    while True:
        todo = ToDo()
        gui = GUi()
        command = input('\nWhat do you want to do? ').lower()

        if command == 'add':
            todo.todo_add()
            gui.main()
            todo.save()
        elif command == 'show':
            todo.show_todo_list()
        elif command == 'help':
            print("\nThe commands are Add, Remove, or Show todo list(or just type show)\n")
        elif command == 'remove':
            todo.show_todo_list()
            delete = int(input('\nWhat line do you want to remove: '))
            todo.remove(delete)
            todo.save()
        elif command == 'quit':
            break
        else:
            print('\nNot valid command (type help for commands)\n')