import PySimpleGUI as PG

lable = PG.Text('welcome')
intup = PG.Input('enter a thing:')
bottun = PG.Button('did')

window = PG.Window('todo>', layout=[[lable], [intup, bottun]])
window.read()
print('here')
window.close()
