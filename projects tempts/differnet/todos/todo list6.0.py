def up_todos():
    with open('todoList6.0', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


name = input('enter your name:')
todos = []
while True:
    command = input('enter a command:')
    wrong = f'{command} is not correct , please try:show/add/edit/done/exit'
    if command.startswith('add'):
        new_todo = command[4:]
        todos = up_todos()
        todos.append(new_todo + '\n')
        with open('todoList6.0', 'w') as file:
            file.writelines(todos)
    elif command.startswith('show'):
        todos = up_todos()
        for index, i in enumerate(todos):
            i = i.strip('\n')
            print(f'{index + 1}_{i}')
    elif command.startswith('edit'):
        try:
            todos = up_todos()
            change = int(command[4:]) - 1
            new_todo = input("enter the new todo:") + '\n'
            todos[change] = new_todo
            with open('todoList6.0', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print(f'the list have only {len(todos)} numbers')
        except ValueError:
            print(wrong)
    elif command.startswith('complete'):
        try:
            todos = up_todos()
            done = int(command[9:]) - 1
            todos.pop(done)
            with open("todoList6.0", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('the command is wrong')
            continue
        except IndexError:
            print('the index is out of range')
            continue
    elif command.startswith('exit'):
        break
    else:
        print(wrong)
print('good luck')
