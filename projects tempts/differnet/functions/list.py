from fuctions import get_todos, write_in_list

while True:
    command = input('enter a command:')
    command = command.strip()
    if command.startswith('add'):
        todos_list = get_todos()
        new_todo = command[4:]
        print(todos_list)
        todos_list.append(new_todo + '\n')

        write_in_list(todos_list)
    elif command.startswith('show'):
        todos_list = get_todos()

        for index, i in enumerate(todos_list):
            index = index + 1
            i = i.strip('\n')
            print(f'{index}_{i}')
    elif command.startswith('complete'):
        try:
            done = int(command[5:]) - 1

            todos_list = get_todos()

            todos_list[done] = todos_list[done] + 'done(*)'

            write_in_list(todos_list)
        except ValueError:
            print('oops. enter number of the todo you see')
    elif command.startswith('exit'):
        break
    else:
        print('wrong.try again')
