class ToDo:            # fix and test everything please i cannot do it right now because i am tired.
    def __init__(self):
        self.lists = []
        self.add = None
        self.counter = 0
        try:
            with open('text.txt', 'r') as f:
                self.lists = f.readlines()
                self.lists = [line.strip() for line in self.lists]
        except FileNotFoundError:
            pass
    
    def todo_add(self):
        addition = input('> ').strip().capitalize()
        self.add = addition
        try:
            with open('text.txt', 'r') as f:
                if self.counter == 0:
                    self.lists = [line.strip() for line in self.lists]
                    self.counter += 1
                elif self.counter >= 1:
                    self.lists = [line + '\n' for line in self.lists]

                if addition in self.lists:
                    print(f"\nYou have already have a task named {addition}.")
                    add_another = input('Add it anyway? (yes/no) ').lower()
                    if add_another == 'yes' or add_another == 'y':
                        self.lists.append(addition)
                        self.lists = [line.rstrip('\n') for line in self.lists]
                        self.counter = 0
                        print(f"Another {addition} Added!")
                        self.counter += 1
                    else:
                        print(f'"{addition}" not added!\n')
                        self.counter += 1
                else:
                    self.lists.append(addition + '\n')
                    print(f'{addition} Added!!\n')
        except FileNotFoundError:
            with open('text.txt', 'a') as f:
                f.write('New file created with the name text.txt')
                print('Created a file that was non-exestant named: text.txt!!')


    def show_todo_list(self):
        try:
            with open('text.txt', 'r') as f:
                tasks = [line.strip() for line in f if line.strip()]
                
                if not tasks:
                    print('No tasks in the list!')
                
                print('\nYour todo list:')
                for i, line in enumerate(tasks, start=1):
                    print(f'{i}. {line}')
        except FileNotFoundError:
            print('No file task found, please add a task!')
            
    def remove(self, number):
        try:
            with open('text.txt', 'r') as f:
                tasks = [line.strip() for line in f if line.strip()]
                index_to_delete = None

                for i, line in enumerate(tasks, start=1):
                    if i == number:
                        index_to_delete = i - 1
                        if self.lists == []:
                            print(f'Line {i}. {line} has been succesfully removed!')
                    else:
                        print('Not valid number in the list!')

                if index_to_delete != None:
                    del tasks[index_to_delete]
                    

        except FileNotFoundError:
            print('No file task found, please add a task!')
        except ValueError:
            print('Please print a number!')

    def save(self):
        with open('text.txt', 'w') as f:
            f.writelines(self.lists)