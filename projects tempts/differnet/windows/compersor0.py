import PySimpleGUI as py
import zip_creator as zip


lable = py.Text('compress some shit')
file_button = py.FilesBrowse('choose some')
what_adderess = py.Input(tooltip='files addresses', key='files_r')

lable2 = py.Text('where to shuvel')
folder_button = py.FolderBrowse('where?')
where_adderss = py.Input(tooltip='address', key='dest_address')

namelable = py.Input(tooltip='enter the name', key='name')

button = py.Button('do')
output = py.Text(key='out', text_color='blue')
window = py.Window('shovel', layout=[[lable, what_adderess, file_button],
                                     [lable2, where_adderss, folder_button], [namelable],
                                     [button, output]], background_color='black')

while True:
    command, paths = window.read()
    print(command, paths)
    filepaths = paths['files_r']
    filepaths = filepaths.split(';')
    name = paths['name']
    zip.make_archive(filepaths, name, dest_filepath=paths['dest_address'])
    window['out'].Update('complete')
    if command == py.CloseButton:
        break
window.close()
