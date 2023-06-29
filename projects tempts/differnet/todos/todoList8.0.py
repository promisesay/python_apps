def get_todos(filepath):
    with open(filepath) as local_file:
        todos = local_file.readlines()
    return todos


def write_todos(filepath, todos):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos)


while True:
    command = input('enter a command:')
    command.strip()
    wrong = f'{command} is not a command. try:edit/add/show/complete/exit'
    if command.startswith('add'):
        try:
            new_todo = command[4:]
            todolist = get_todos('todoList8.0.txt')

            todolist.append(new_todo + '\n')

            write_todos('todoList8.0.txt', todolist)
        except ValueError:
            print(f'try a number after {command}')
    elif command.startswith('show'):
        todolist = get_todos('todoList8.0.txt')

        for index, i in enumerate(todolist):
            i = i.strip('\n')
            todo = f'{index + 1}_{i}'
            print(todo)

    elif command.startswith('edit'):
        try:
            todolist = get_todos('todoList8.0.txt')

            change = int(command[4:]) - 1
            new_todo = input('enter new todo:')
            todolist[change] = new_todo

            write_todos('todoList8.0.txt', todolist)
        except ValueError:
            print(f'try a number after {command}')
            continue
        except IndexError:
            print(f'the {change} is out of range , the list have just{len(todolist)}')
    elif command.startswith('complete'):
        try:
            todolist = get_todos('todoList8.0.py')

            remove = int(command[9:])
            todolist.pop(remove)

            write_todos('todoList8.0.txt', todolist)
        except ValueError:
            print(f'try a number after {command}')
            continue
    elif command.startswith('exit'):
        break
    else:
        print(wrong)
print('good luck and keep up the discipline')
