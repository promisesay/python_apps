FILE = '../Files/data.txt'


def reader(items, filepath=FILE):
    with open(filepath, 'r') as locally:
        items = locally.readlines()
        return items


def writer(items, filepath=FILE):
    with open(filepath, 'w') as inner:
        inner.writelines(items)

