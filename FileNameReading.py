# function to get all of the files names, returns a dictionary
def get_file_names():
    f = open("filenames.txt", "r")

    t = f.read()

    l = t.split('\n')

    sensor_names = {}
    count = 0;

    for name in l:
        if name == 'NULL':
            continue
        elif name == 'FileName':
            continue
        else:
            sensor_names[name] = count
            count +=  1

    return sensor_names



