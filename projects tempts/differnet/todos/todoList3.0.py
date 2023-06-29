userName: str = input('enter your name please:')
todoList3 = []
while True:
    command = input("enter a command:")
    if "not" not in command:
        todo = input("enter a new todo:") + "\n"
        file = open('todoList3.0.txt', 'r')
        todoList3 = file.readlines()
        file.close()

        todoList3.append(todo)

        file = open('todoList3.0.txt', 'w')
        file.writelines(todoList3)
        file.close()
    elif "show" in command:
        file = open('todoList3.0.txt', 'r')
        todoList3 = file.readlines()
        file.close()

        for index, i in enumerate(todoList3):
         print(f"{index}_{i}")
    elif "complete" in command:
        done=int(input("enter the index:"))
        todoList3.pop(done)
        file = open('todoList3.0.txt', 'w')
        file.writelines(todoList3)
        file.close()
    elif "edit" in command:
        newTodo = input("enter new todo:")
        change = int(input("enter the index of the changing todo:"))
        todoList3[change] = newTodo
        file = open(r'/different/todoList3.0.txt', 'w')
        file.writelines(todoList3)
        file.close()
    elif "exit" in command:
        break
    else:
        print(f"{command} is a none command please  try:add/show/complete/edit or exit.")
print(f"goode luck {userName}")