from todo_class import ToDo
"""
I added a thing called line_counter it defintantley need refining please go over this and fix anything 
in the add and remove functions (or any function for that matter)

ps: i currently don't have time to do this right now it is 23:33 hours on aug 6

i worked on this today it is aug 11 time: 00:16 year: 2025
My faut i have been working o0n this but i forgot to log my hours so i will do that today. Time: 22:08 9/4/2025

17 September 2025: I couldn't work on this today after hearing the news that comick shut down a day prior: I hate my life hopefully they can get back on but i highly doudt that after all they said they weren't going to come back.
sep 18-Started using a new site called Mangapark: but i am afraid that this site nor any other can compare to the feeling and community of comick and from the look of things its translations aren't that good either
sep 21- i found a new site called MangaFire and its translations are pretty good
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