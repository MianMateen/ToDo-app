class ToDo:            # fix and test everything please i cannot do it right now because i am tired.
    def __init__(self):
        self.lists = []
    
    def todo_add(self):
        self.add = input('> ')
        with open('text.txt', 'r') as f:
            lines = f.readlines()
            if self.add in lines:
                print(f"You have already have a task named {self.add}")
                add_another = input('Are you sure you want to add another one? ').lower()
                if add_another == 'yes' or add_another == 'y':
                    self.lists.append(self.add + '\n')
                    print(f"Another {self.add} Added!\n")
                elif add_another == 'no' or add_another == 'n':
                    print(f'{self.add} not added!\n')
            elif self.add not in lines:
                self.lists.append(self.add + '\n')
                print(f'{self.add} Added!!\n')


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