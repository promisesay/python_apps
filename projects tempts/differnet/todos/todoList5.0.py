userName = input("Enter the name:")
todoList = []
while True:
    user_command = input("enter a command:")
    user_command = user_command.strip()
    if 'add' in user_command:
        with open('todoList5.0.txt', 'r') as file:
            todoList = file.readlines()
        todoList.append(user_command[4:] + '\n')
        with open('todoList5.0.txt', 'w') as file:
            file.writelines(todoList)
    elif 'show' in user_command:
        with open('todoList5.0.txt', 'r') as file:
            todoList = file.readlines()
            for index, i in enumerate(todoList):
                i = i.strip('\n')
                index = index + 1
                print(f"{index}_{i}")
        with open('todoList5.0.txt', 'w') as file:
            file.writelines(todoList)
    elif 'edit' in user_command:
        with open('todList5.0.txt', 'r') as file:
            todoList = file.readlines()
        number = int(user_command[5:]) - 1
        new_todo = input('enter new todo:')
        todoList[number] = new_todo + '\n'
        with open('todoList5.0.txt', 'w') as file:
            file.writelines(todoList)
    elif 'done' in user_command:
        with open('todoList5.0.txt', 'r') as file:
            todoList = file.readlines()
        number = int(user_command[5:]) - 1
        todoList.pop(number)
        with open('todoList5.0.txt', 'w') as file:
            file.writelines(todoList)
    elif 'exit' in user_command:
        break

    else:
       print(f'{user_command} is not a command')
print(f'Good Luck today {userName}')
