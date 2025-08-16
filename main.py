from todo_class import ToDo
"""
I added a thing called line_counter it defintantley need refining please go over this and fix anything 
in the add and remove functions (or any function for that matter)

ps: i currently don't have time to do this right now it is 23:33 hours on aug 6

i worked on this today it is aug 11 time: 00:16 year: 2025
"""

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
            delete = int(input('\nWhat line do you want to remove: '))
            todo.remove(delete)
            todo.save()
        elif command == 'quit':
            break
        else:
            print('\nNot valid command (type help for commands)\n')