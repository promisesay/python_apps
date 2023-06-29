def writing(new, filepath='todoList9.0.txt'):
    with open(filepath, 'w') as filelocally:
        filelocally.writelines(new)


def reading(new, filepath='todoList9.0.txt'):
    with open(filepath, 'r') as fileloccally:
        new = fileloccally.readlines()
        return new


while True:
    command = input('enter a command:')
    todos = []
    if command.startswith('add'):
        todos = reading(todos)

        todos.append(command[4:] + "\n")

        writing(todos)
    elif command.startswith("show"):
        todos = reading(todos)
        for index, i in enumerate(todos):
            row = f'{index + 1}_{i}'
            row = row.strip('\n')
            print(row)
        writing(todos)
    elif command.startswith("remove"):
        reading(todos)

        done = int(command[7:]) - 1
        todos.pop(done)

        writing(todos)
    elif command.startswith('exit'):
        break
    else:
        print('please try again')

