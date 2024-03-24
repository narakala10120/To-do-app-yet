# Function to read the todos

def get_todos(filepath='todo.txt'):
    """ Read a text file and return 
    the list of to-do items"""
    with open(filepath, 'r') as file:
          todos = file.readlines()
    return todos


# Function to write the todos


def write_todos( todos_arg, filepath='todo.txt'):
     """Write the todo items list in the tetx file"""
     with open(filepath, 'w') as file:
          file.writelines(todos_arg)

print("Using Functions now")
# This is used to run the function file individually, if you want to check anything as such, but when you execute the main.py
# The lines under the if conditions will not be executes.
if __name__ == "__main__":
     print("Hello from functions")