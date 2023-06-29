userName = input("enter you're name:")
todoList = []
while True:
    command = input(f"enter a command {userName}:")
    command.strip()
    command.title()
    match command:
        case 'add':
            with open('todoList4.0.txt', 'r') as file:
                todoList = file.readlines()

            many = int(input("how many?"))
            for i in range(many):
                new_todo = input("enter new todo:") + '\n'
                todoList.append(new_todo + "don't smoke weed!!")

            with open('todoList4.0.txt', 'w') as file:
                file.writelines(todoList)
        case 'show':
            with open('todoList4.0.txt', 'r') as file:
                todoList = file.readlines()

            #new_todo = [i.strip('\n') for i in todoList]
            for index, i in enumerate(todoList):
                i = i.strip('\n')#you should espesfie the i.strip() is done for what
                row = f'{index+1}_{i}'
                print(row)
        case 'exit':
            break
        case 'edit':
            many = int(input('how many:'))
            for i in range(many):
                remove = int(input('enter the index:')) - 1
                change = input('enter the new todo:') + '\n'
                todoList[remove] = change
            with open('todoList4.0.txt', 'w') as file:
                file.writelines(todoList)
        case 'done':
            with open('todoList4.0.txt', 'r') as file:
                todoList = file.readlines()
            many = int(input('how many?'))
            done = int(input('enter the index of todo:'))
            index = done - 1

            todoList.pop(index)
            for i in range(many):
                if many > 1:
                    done = int(input('and:'))

                    todoList.pop(index)
            with open('todoList4.0.txt', 'w') as file:
                file.writelines(todoList)
        case none:
            print(f'{none} is not a command')

print(f'goodluck {userName}')