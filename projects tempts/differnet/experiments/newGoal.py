import glob
import zipWritingfiles


def check_goal(new, filepath):
    new = new.capitalize()
    names = glob.glob(fr'../{filepath}/*.txt')
    for i in names:
        if new == i:
            newfilepath: str = fr'{filepath}/{i}'
            with open(newfilepath) as file:
                new = file.readlines()
                return new
    """check if the file is already in the file or not 
    and if it is the file content will be read by the new list"""


if __name__ == '__main__':
    name = input('enter the name:')
    reasons = check_goal(name, 'files')
    print(reasons)
    reason = input('enter new reason:')
    reasons.append(reason)
    zipWritingfiles.write_files(f'files/{name}.txt', reasons)
