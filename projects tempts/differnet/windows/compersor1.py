from ..experiments.zipWritingfiles import filereader, write_file
import PySimpleGUI

lable = PySimpleGUI.Text('comperesor')
broswer = PySimpleGUI.FileBrowse('choose folder')
bottun = PySimpleGUI.Input()

lable2 = PySimpleGUI.Text('Choose file')
broswer2 = PySimpleGUI.FolderBrowse('choose destination')
bottun2 = PySimpleGUI.Input()

bottun3 = PySimpleGUI.Button('comperes')

window = PySimpleGUI.Window('compressor', layout=[[lable2, broswer, bottun2],
                                                  [lable, broswer2, bottun],
                                                  [bottun3]])
events = []
event = window.read()
for i in event:
    print(i)
filereader(events)
events.append(event)
write_file(events)
window.close()
