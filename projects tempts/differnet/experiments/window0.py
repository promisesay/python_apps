import PySimpleGUI as py

lable = py.Text('hellow')
intup = py.Input('enter a thing:')

window = py.Window('str', layout=[[lable, intup]])
window.read()
window.close()