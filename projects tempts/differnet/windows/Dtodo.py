import doread
import PySimpleGUI as pg


todolist = []
lable = pg.Text('enter:')
input1 = pg.Input(tooltip='enter a todo', key='todo', size=[20, 5])
button = pg.Button('add')
button2 = pg.Button('exit')
button3 = pg.Button('complete')
edit_button = pg.Button('edit')
radiff = pg.Listbox(values=doread.reader(), key='todos',
                    enable_events=True, size=[27, 6])
window = pg.Window('todos', layout=[[lable, input1],
                                    [button, button3], [radiff, button2, edit_button]],
                   font=('Helvetica', 15)
                   )

while True:
    command, new = window.read()
    print(command)
    print(new)

    match command:
        case 'add':
            todolist = doread.reader()
            new_todo = new['todo'] + '\n'
            todolist.append(new_todo)
            doread.writer(todolist)
            window['todos'].Update(values=todolist)
        case 'complete':
            todolist = doread.reader()
            done = new['todos']
            pack = done[0]
            print(pack)
            todolist.remove(pack)
            doread.writer(todolist)
            window['todos'].Update(values=todolist)
        case 'edit':
            todolist = doread.reader()
            change = new['todos'][0]
            done = todolist.index(change)
            wit = new['todo']
            todolist[done] = wit
            doread.writer(todolist)
            window['todos'].Update(values=todolist)
        case 'todos':
            todolist = doread.reader()
            item = new['todos'][0]
            window['todo'].update(value=item)

        case pg.WINDOW_CLOSED:
            break
        case 'exit':
            break
