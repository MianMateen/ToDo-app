class ToDo:            # fix and test everything please i cannot do it right now because i am tired.
    def __init__(self):
        self.lists = []
        self.add = None
        self.line_counter = 0
        try:
            with open('text.txt', 'r') as f:
                self.lists = f.readlines()
        except FileNotFoundError:
            pass
    
    def todo_add(self):
        addition = input('> ').strip().capitalize()
        self.add = addition
        self.line_counter += 1
        for line in self.lists:
            line.strip()
            
        if addition in self.lists:
            print(f"\nYou have already have a task named {addition}.")
            add_another = input('Add it anyway? (yes/no) ').lower()
            self.line_counter = str(self.line_counter)
            if add_another == 'yes' or add_another == 'y':
                self.lists.append(self.line_counter + addition)
                print(f"Another {addition} Added!")
            else:
                print(f'"{addition}" not added!\n')
        else:
            self.line_counter = str(self.line_counter)
            self.lists.append(self.line_counter + '.' + ' ' + addition + '\n')
            print(f'{addition} Added!!\n')
            save()



    def show_todo_list(self):
    
        if not self.lists:
            print('No tasks in the list!')
        
        print('\nYour todo list:')
        for line in self.lists:
            print(line)


    def remove(self, number):
        try:

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
                    
        except ValueError:
            print('Please print a number!')

    def save(self):
        with open('text.txt', 'w') as f:
            f.writelines(self.lists)