class ToDo:
    def __init__(self):
        self.lists = []
    
    def todo_add(self):
        self.add = input('> ')
        self.lists.append(self.add)


    def show_todo_list(self):
        with open('text.txt', 'r') as f:
            for task in f:
                print(task, end=' ')


    def save(self):
        with open('text.txt', 'a') as f:
            fContents = f.writelines(self.lists)


while True:
    command = input('\nWhat do you want to do? ').lower()
    todo = ToDo()

    if command == 'add':
        todo.todo_add()
    elif command in ['show todo', 'show', 'show todo list']:
        todo.show_todo_list()
    elif command == 'help':
        print("\nThe commands are Add, Remove, Save, or Show todo list(or just type show)\n")
    elif command == 'save':
        todo.save()
    elif command == 'quit':
        break
    else:
        print('\nNot valid command (type help for commands)\n')