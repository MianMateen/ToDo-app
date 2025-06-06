lists = []
while True:
    command = input("Say something: ").lower()

    if command == 'add':
        add = input("> ")
        lists.append(add + '\n')
        
        with open('test.txt', 'r') as file_read:
            read = file_read.readlines()  # This doesn't work fix it later
            if add in read:  
                print(f"\nCant add another todo named {add}\n")
            elif add not in read:
                print(f'Added {add}!!!\n')

    elif command == "save":
        with open('test.txt', 'a') as f:
            fcon = f.writelines(lists)
            print(lists)
    elif command == 'exit':
        break