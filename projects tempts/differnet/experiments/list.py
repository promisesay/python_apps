from functions import fuctions

while True:
    command = input('enter a command:')
    command = command.strip()
    if command.startswith('add'):
        todos_list = fuctions.get_todos()
        new_todo = command[4:]

        todos_list.append(new_todo + '\n')

        fuctions.write_in_todos(todos_list)
    elif command.startswith('show'):
        todos_list = fuctions.get_todos()

        for index, i in enumerate(todos_list):
            index = index + 1
            i = i.strip('\n')
            print(f'{index}_{i}')
    elif command.startswith('complete'):
        try:
            done = int(command[5:]) - 1

            todos_list = fuctions.get_todos()

            todos_list[done] = todos_list[done] + 'done(*)'

            fuctions.write_in_list(todos_list)
        except ValueError:
            print('oobs. enter number of the todo you see')
    elif command.startswith('exit'):
        break
    else:
        print('wrong.try again')