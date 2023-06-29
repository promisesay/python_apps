def get_todos(filepath=r'C:\Users\Navid\AppData\Roaming\JetBrains\PyCharm2022.2\extensions\differnet\todos\list_of_works.txt'):
    """ a function for calling the local list on the system
    for checking and updating the list of works """
    with open(filepath, 'r') as local_file:
        works = local_file.readlines()
    return works
def forward(dark):

    dark = dark.replace('/', )
    return dark



tar = input('whats the link?')
forward(tar)

def write_in_list(new_list, filepath=r'..\differnet\todos\list_of_works.txt'):
    """ a function for saving the changes on the list in\n"
     "the system """
    with open(filepath, 'w') as file_locally:
        file_locally.writelines(new_list)



