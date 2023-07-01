FILEPATH = 'files/new.txt'


def write_files(lists, filepath=FILEPATH):
    for file, lists in zip(filepath, lists):
        with open(filepath, 'w') as file_locally:
            file_locally.writelines(lists)


def write_file(list, filepath=FILEPATH):
    with open(filepath, 'r') as local_file:
        local_file.writelines(list)


def filereader(items, filepath=FILEPATH):
    with open(filepath, 'r') as local_file:
        items = local_file.readlines()
        return items


if __name__ == '__main__':
    job = []
    new = input('enter:')
    if new.startswith('read'):
        filereader(job)
        print(job)
    else:
        job.append(new)
        write_files(job, fr'files/{new}.txt')
