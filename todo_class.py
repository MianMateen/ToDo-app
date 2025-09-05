class ToDo:            
    def __init__(self):
        self.lists = []
        self.number_list = list(range(1, 51))
        self.add = None
        self.line_counter_file = 'line_counter.txt'
        self.add_called = False
        try:
            with open(self.line_counter_file, 'r') as f:
                self.line_counter = int(f.read())
            with open('text.txt', 'r') as f:
                self.lists = f.readlines()
        except FileNotFoundError:
            pass
    
    def todo_add(self):
        self.add_called = True
        addition = input('> ').strip().capitalize()
        self.line_counter += 1
        
        existing_lists = [task.split('. ', 1)[1].strip() for task in self.lists if '. ' in task]
        if addition in existing_lists:
            print(f"\nYou have already have a task named {addition}.")
            add_another = input('Add it anyway? (yes/no) ').lower()
            if add_another == 'yes' or add_another == 'y':
                self.lists.append(f"{self.line_counter}. {addition}\n")
                print(f"Another '{addition}' Added!\n")
                self.save()
                return 0
            else:
                 print(f'"{addition}" not added!\n')
                 self.line_counter -= 1
                 return 1
        else:
            self.lists.append(f'{self.line_counter}. {addition}\n')
            print(f'"{addition}" Added!!\n')
            self.save()
            return 0


    def show_todo_list(self):
    
        if not self.lists:
            print('No tasks in the list!')
        
        print('\nYour todo list:')
        for line in self.lists:
            print(line)


    def remove(self, number):
        try:

            for i, task in enumerate(self.lists):
                if task.startswith(f'{number}. '):
                    removed_task = self.lists.pop(i)
                    self.line_counter -= 1
                    print(f'Removed: {removed_task}')
                    self.number_assortment()
                    self.save()
                    return
                
            print(f"Task {number} not found")
                    
        except ValueError:
            print('Please print a number!')
            
    def number_assortment(self):
        self.lists = [f'{i+1}. {tasks.split('. ', 1)[1]}' for i, tasks in enumerate(self.lists)]
        self.line_counter = len(self.lists)

    def save(self):
        with open('text.txt', 'w') as f:
            f.writelines(self.lists)
            
        with open(self.line_counter_file, 'w') as f:
            f.write(str(self.line_counter))