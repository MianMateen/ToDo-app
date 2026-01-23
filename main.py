from todo_class import ToDo

if __name__ == '__main__':
    while True:
        todo = ToDo()
        command = input('\nWhat do you want to do? ').lower()

        if command == 'add':
            todo.todo_add()
            todo.save()
        elif command == 'show':
            todo.show_todo_list()
        elif command == 'help':
            print("\nThe commands are Add, Remove, or Show todo list(or just type show)\n")
        elif command == 'remove':
            todo.show_todo_list()
            while True:
                usr_input = input('\nWhat line do you want to remove (q to quit): ')
                if usr_input == 'q':
                    print("Quitting program")
                    break
                try:
                    usr_delete = int(usr_input)
                    if usr_delete <= 0:
                        print('Can only put a non-negative integer (including 0)')
                        break
                    todo.remove(usr_delete)
                    todo.save()
                except ValueError:
                    print('Can only type in a integer')
        elif command == 'quit':
            break
        else:
            print('\nNot valid command (type help for commands)\n')
