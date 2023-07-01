import doread
import PySimpleGUI as pg

lable = pg.Text('enter:')
input1 = pg.Input(tooltip='enter a todo', key='todo')
button = pg.Button('add')
button2 = pg.Button('edit')
button3 = pg.Button('complete')
window = pg.Window('todos', layout=[[lable, input1],
                                    ],
                   font=('Helvetica', 20))
todos = []
while True:
    add, new = window.read()
    print(add)
    print(new)

    match add:
        case 'add':
            todos = doread.reader(todos)
            new_todo = new['todo'] + '\n'
            todos.append(new_todo)
            doread.writer(todos)
        case pg.WINDOW_CLOSED:
            break
