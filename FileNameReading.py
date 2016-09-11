# function to get all of the files names, returns a dictionary
def get_file_names():
    # two options, all_sensors.txt or some_sensors.txt
    f = open("some_sensors.txt", "r")

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
            count += 1

    return sensor_names



