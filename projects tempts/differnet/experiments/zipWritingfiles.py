def write_files(filepath, lists):
    for file, lists in zip(filepath, lists):
        with open(filepath, 'w') as file_locally:
            file_locally.writelines(lists)


if __name__ == '__main__':
    job = []
    new = input('enter:')
    job.append(new)
    write_files(fr'files/{new}.txt', job)
