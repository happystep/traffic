# function to get all of the files names for testing southbound data.
def get_file_names():
    f = open("filenames.txt", "r")

    t = f.read()

    l = t.split('\n')

    files = []

    for x in l:
        if x == 'NULL':
            continue
        elif x == 'FileName':
            continue
        else:
            files.append(x)
    return files

