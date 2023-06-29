def read_reasons(filepath):
    with open(filepath, 'r') as file_locally:
        rest = file_locally.readlines()
    return rest


def write_files(filepath, results):
    with open(filepath, 'w') as file_in:
        file_in.writelines(results)


def files_in(filepath, data):
    for files, data in zip(filepath, data):
        print(files)


files_in(r'C:\Users\Navid\PycharmProjects\pythonProject\projects tempts\differnet\journals', 'fonn')


goal = input('enter the goal')
vision = input('enter your vision of what gonna happen if you reach it:')
reason = input(f'enter you reason for {goal}')
