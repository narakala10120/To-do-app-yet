# importing modules 
from functions import get_todos, write_todos
import time
# import functions
# Enter the loop
now = time.strftime("%b %d, %Y %H:%M")
print(f"It is {now}")
while True:
    user_action = input("add/show/complete/edit/exit :")
    user_action = user_action.strip()

    # Adds the todo into todos
    
    if user_action.startswith('add'):
        
        todo = user_action[4:]+ "\n"
            

        todos = get_todos()


        todos.append(todo.capitalize())

        write_todos(filepath='todo.txt', todos_arg=todos)

        
            # Overwrites the files into new ones
            
        # show the todos from the file
    elif user_action.startswith('show'):
        
        todos = get_todos()


        for index,item in enumerate(todos):
            print(f"{index + 1}-{item.strip()}")

    #  edit -- By list indexing -- it helps you to reenter a new value into the list
    elif user_action.startswith('edit'):

        

        try:
            item_to_edit = int(user_action[5:])
            todos = get_todos()
            
        
            todos[item_to_edit-1] = input("Enter the new todo:").capitalize() + '\n'
            

            write_todos(filepath='todo.txt', todos_arg=todos)
        except ValueError:
            print('Your commnad is not valid')
            continue
            # Helps to complete the lsit of items
    elif  user_action.startswith('complete'):
            try:
                items_completed = int(user_action[9:])

                todos = get_todos()
                index = items_completed - 1
                to_do_remove = todos[index]
                todos.pop(items_completed-1)

                write_todos(filepath='todo.txt', todos_arg=todos)

                print(f"Todo {to_do_remove.strip()} has been completed successfully")
            except IndexError:
                 print('There is no item with that number')

        
    else:
            break

print('bye')
