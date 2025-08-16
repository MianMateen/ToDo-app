
class ToDo:            # fix and test everything please i cannot do it right now because i am tired.
    def __init__(self):
        self.lists = []
        self.number_list = list(range(1, 51))
        self.add = None
        self.line_counter_file = 'line_counter.txt'
        try:
            with open(self.line_counter_file, 'r') as f:
                self.line_counter = int(f.read())
            with open('text.txt', 'r') as f:
                self.lists = f.readlines()
        except FileNotFoundError:
            pass
    
    def todo_add(self):
        addition = input('> ').strip().capitalize()
        self.line_counter += 1
        
        existing_lists = [task.split('. ', 1)[1].strip() for task in self.lists if '. ' in task]
        if addition in existing_lists:
            print(f"\nYou have already have a task named {addition}.")
            add_another = input('Add it anyway? (yes/no) ').lower()
            if add_another == 'yes' or add_another == 'y':
                self.lists.append(f"{self.line_counter}. {addition}\n")
                print(f"Another '{addition}' Added!\n")
            else:
                 print(f'"{addition}" not added!\n')
                 self.line_counter -= 1
        else:
            self.lists.append(f'{self.line_counter}. {addition}\n')
            print(f'"{addition}" Added!!\n')
            
        with open(self.line_counter_file, 'w') as f:
            f.write(str(self.line_counter))


    def show_todo_list(self):
    
        if not self.lists:
            print('No tasks in the list!')
        
        print('\nYour todo list:')
        for line in self.lists:
            print(line)


    def remove(self, number):
        try:

            ListOfNumbers = [int(task.split('. ', 1)[0].strip()) for task in self.lists if '. ' in task]
            index_to_delete = number

            if index_to_delete in ListOfNumbers:
                index_to_delete -= 1
                del ListOfNumbers[index_to_delete]
                print(f'Deleted "{ListOfNumbers}"')
            else:
                print(f"Didn't delete {ListOfNumbers}")
                    
        except ValueError:
            print('Please print a number!')

    def save(self):
        with open('text.txt', 'w') as f:
            f.writelines(self.lists)