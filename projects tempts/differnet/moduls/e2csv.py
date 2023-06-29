import csv

with open("../todos/todoList4.0.txt", 'r') as file:
    mike = list(csv.reader(file))

print(mike)
capital = input('enter:')
capital = capital.capitalize()
print(capital)
for i in mike[1:]:
    if capital == i[0]:
        print(i[1])

