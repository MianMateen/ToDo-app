lists = []
command = input("Say something: ").lower()
if command == 'add':
    with open('test.txt', 'a') as f:
        lists.append(command + '\n')
        fcon = f.writelines(lists)
elif command == "save":
    with open('test.txt', 'a') as f:
        fcon = f.writelines(lists)
        print(fcon)

for item in lists:
    if item in lists:  
        print(f"\nCant add another todo named {item}\n")