import PySimpleGUI
import zip_creator
filepath = 'addresses.txt'
Text = PySimpleGUI.Text('compressor')
file_browser = PySimpleGUI.FilesBrowse('choose file', key='file addresses')
files_address = PySimpleGUI.Input(tooltip='enter the address', key='files')

Text2 = PySimpleGUI.Text('Choose file')
folder_browser = PySimpleGUI.FolderBrowse('choose destination')
dest_address = PySimpleGUI.Input(tooltip='enter', key='dest_address')

compress_button = PySimpleGUI.Button('comperes')

window = PySimpleGUI.Window('compressor',
                            layout=[[Text2, files_address, file_browser],
                                    [Text, dest_address, folder_browser],
                                    [compress_button]])


while True:
    event, values = window.read()
    if event == 'comperes':
        paths = values['files']
        dest_path = values['dest_address']
        paths = paths.split(';')
        zip_creator.make_archive(paths, dest_path)
    elif event == PySimpleGUI.WINDOW_CLOSED:
        break
window.close()
