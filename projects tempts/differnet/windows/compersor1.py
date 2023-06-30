import PySimpleGUI

lable = PySimpleGUI.Text('comperesor')
broswer = PySimpleGUI.FileBrowse('choose folder')
bottun = PySimpleGUI.Input()

lable2 = PySimpleGUI.Text('Choose file')
broswer2 = PySimpleGUI.FolderBrowse('choose destination')
bottun2 = PySimpleGUI.Input()

bottun3 = PySimpleGUI.Text('comperes')
window = PySimpleGUI.Window('compersore', layout=[[lable2, broswer2, bottun2],
                            [lable, broswer, bottun], [bottun3]])
