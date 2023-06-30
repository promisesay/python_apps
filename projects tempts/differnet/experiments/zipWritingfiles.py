def write_files(filepath, lists):
    for file, lists in zip(filepath, lists):
        with open(filepath, 'w') as file_locally:
            file_locally.writelines(lists)


def write_file(filepath, list):
    with open(filepath, 'r') as local_file:
        local_file.writelines(list)


def filereader(filepath, items):
    with open(filepath, 'r') as local_file:
        items = local_file.readlines()
        return items


if __name__ == '__main__':
    job = []
    new = input('enter:')
    job.append(new)
    write_files(fr'files/{new}.txt', job)
