import csv


class FileOperation:
    csvfile_name = 'worklog.csv'
    csvfile_mode = 'a'

    with open(csvfile_name, mode=csvfile_mode) as csvfile:
        print(csv.DictReader(csvfile))


class Add(FileOperation):
    pass


class Edit(FileOperation):
    pass


class Delete(FileOperation):
    pass