def get_todos(filepath):
    with open(filepath) as local_file:
        todos_local = local_file.readlines()
    return todos_local


def in_todos(filepath, todos_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


todoList = []
while True:
    user_command = input('enter a command:')
    user_command.strip()
    if user_command.startswith('add'):
        todoList = get_todos('todoList7.0.txt')

        user_command = user_command[4:]
        print(user_command)

        todoList.append(user_command + '\n')
        in_todos('todoList7.0.txt', todoList)
    elif user_command.startswith('show'):
        todoList = get_todos('todoList7.0.txt')

        for index, i in enumerate(todoList):
            i = i.strip('\n')
            print(f'{index + 1}_{i}')
    elif user_command.startswith('edit'):
        try:
            todoList = get_todos('todoList7.0.txt')

            user_command = int(user_command[5:]) - 1

            new_todo = input('enter a new todo:')

            todoList[user_command] = new_todo

            in_todos('todoList7.0.txt', todoList)
        except ValueError:
            print('wrong input after command please enter the number of todo')
            continue
    elif user_command.startswith('complete'):
        try:
            todoList = get_todos('todoList7.0.txt')

            remove = int(user_command[9:]) - 1
            todoList.pop(remove)

            in_todos('todoList7.0.txt', todoList)
        except ValueError:
            print('there is an issue in your command ')
            continue
    elif user_command.startswith('exit'):
        break
    else:
        print('wrong command!')
print('good luck')
