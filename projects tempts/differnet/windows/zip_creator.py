import zipfile
import pathlib


def make_archive(files, name, dest_filepath):
    dest_filepath = pathlib.Path(dest_filepath, 'comperess')
    with zipfile.ZipFile(dest_filepath, 'w') as archive:
        for file in files:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)


if __name__ == "__main__":
    fileL = ["d1.py", "d2.py", "window.py"]
    dest = 'dest'
    make_archive(fileL, dest)

