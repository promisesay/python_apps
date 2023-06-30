import PySimpleGUI as sg

lable = sg.Text('choose files')
itup = sg.Input()
browser = sg.FileBrowse('choose')

lable1 = sg.Text('choose destination')
itup1 = sg.Input()
browser2 = sg.FolderBrowse('choose')

button = sg.Button('comperes')

window = sg.Window('window', layout=[[lable, itup, browser], [lable1, itup1, browser2],
                                     [button]])
window.read()
window.close()
