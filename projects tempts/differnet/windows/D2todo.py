import PySimpleGUI as ps
import doread
filepath = 'things.txt'

things = []
lable = ps.Text('say somthing')
input_line = ps.Input(tooltip='here', key='input', size=[19, 4])
button = ps.Button('something')
button2 = ps.Button('somthing')
button3 = ps.Button('more something')
button4 = ps.Button('still something')
squre = ps.Listbox(doread.reader(filepath), key='all',
                   enable_events=True, size=(18, 12))
window = ps.Window('most things', layout=[[lable], [button, input_line],
                                          [button2, button4, squre], [button3]])
print(squre)

while True:
    some, thing = window.read()
    match some:
        case 'something':
            things = doread.reader(filepath)
            thin = thing['input']
            things.append(thin + '\n')
            doread.writer(things, filepath)
            window['all'].Update(things)
        case 'somthing':
            things = doread.reader(filepath)
            if len(things) >= 2:
                rem = len(things)/2
                rim = round(len(things) - (rem - 1))
                things.pop(rim)
                window['all'].Update(things)
                doread.writer(things, filepath)
        case 'still something':
            things = doread.reader(filepath)
            moll = 'bullshit'
            rim = len(things)/2
            rem = round(rim)
            window['all'].Update(things)
            doread.writer(things, filepath)
        case ps.WINDOW_CLOSED:
            break

window.close()
        #as it's naccessry to put close method at the end of the program