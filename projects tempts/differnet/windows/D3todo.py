import PySimpleGUI as pi
import doread

FILE = 'things.txt'
cara = []
lable = pi.Text('todos')
inpot = pi.Input(tooltip='enter a todo', key='new_todo')
butt = pi.Button('add')
todos = pi.Listbox(doread.reader(filepath=FILE), enable_events=True, key='existing', size=[33, 23])
butt2 = pi.Button('edit')
butt3 = pi.Button('complete')
window = pi.Window('todo app', layout=[[lable, inpot, butt3, butt], [todos, butt2]])
while True:
    command, new = window.read()
    print(command)
    print(new)
    match command:
        case 'existing':
            try:
                item = new['existing'][0]
                item = item.strip('\n')
                window['new_todo'].Update(item)
            except IndexError:
                continue
        case 'add':
            try:
                new_todo = new['new_todo']
                cara = doread.reader(FILE)
                cara.append(new_todo + '\n')
                doread.writer(cara, FILE)
                window['existing'].Update(values=cara)
            except IndexError:
                continue
        case 'edit':
            try:
                todo = new['existing']
                cara = doread.reader(FILE)
                change = cara.index(todo)
                cara[change] = todo
                cara.append(todo + '\n')
                doread.writer(cara, FILE)
                window['existing'].Update(values=cara)
            except IndexError:
                continue
            except ValueError:
                print(f'{todo} is not in the list')
        case pi.WINDOW_CLOSED:
            break
        case 'complete':
            try:
                todo = new['new_todo']
                todo = todo + '\n'
                cara = doread.reader(FILE)
                todo = cara.index(todo)
                cara.pop(todo)
                doread.writer(cara, FILE)
                window['existing'].Update(values=cara)
            except IndexError:
                continue
            except ValueError:
                print(f"{todo} is not in the list")
                continue
        case 'exit':
            break
window.close()
