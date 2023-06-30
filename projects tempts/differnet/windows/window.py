import PySimpleGUI as sg

label = sg.Text('lim')
live = sg.Input('help')

show = sg.Window('faith', layout=[[label, live]])
show.read()
show.close()
