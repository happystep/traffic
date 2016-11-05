import FileNameReading, Parsing, Structure, Functions, Clean
import matplotlib.pyplot as plt
import datetime
import numpy as np


# dictionary that contains all the filenames
filenames = FileNameReading.get_file_names()

all_sensors = []

for i in filenames.keys():
    current_sensor = []

    data = Parsing.parse(i)
    print("Current file being read is " + i)
    data = Clean.remove_empty(data)
    for row in data:
        for k, v in row.items():
            if k == "Timestamp":
                line = row[k].split(' ')
                second_value = line[1].split('A') or line[1].split('P')
                row[k] = ((line[0]), (second_value[0]))
                # row[k] = (v, str(v))
        current_sensor.append(row)
        # datetime.datetime.strptime()
    all_sensors.append(current_sensor)

# print(all_sensors)

x = []
y = []

a_list = all_sensors[0]

for a_dict in a_list:
    for key, value in a_dict.items():
        if key == "Timestamp":
            line = value[1].split(':')
            newline = line[0] + line[1]
            x.append(int(newline))
        elif key == "VPH":
            y.append(int(value))

difference = len(x) - len(y)
if difference != 0:
    for dummyvalue in range(0, difference + 1):
        y.append(-1)


x_new  = np.asarray(x)
y_new = np.asarray(y)

plt.plot(x_new, y_new)
#plt.plot(x,y);
#plt.show()




# classmethod datetime.strptime(date_string, format)
# Return a datetime corresponding to date_string, parsed according to format. This is equivalent to datetime(*(time.strptime(date_string, format)[0:6])). ValueError is raised if the date_string and format can’t be parsed by time.strptime() or if it returns a value which isn’t a time tuple. For a complete list of formatting directives, see section strftime() and strptime() Behavior.


#yearData = []
#start = 0
#end = 288
# 2012 was a leap year so it had 366 days, so that will be our loop
#for x in range(0, 366):

#   now = Functions.LoopDay(start, end, all_sensors)
#    start = end +1
#    end = end + 288
#    yearData.append(now)

#for n in yearData:
#    print(n)









#
# currentDict = saved[0]
#
#
# s = Structure.StationData(" "," "," "," "," "," "," "," ") #figure out better NULL initialization of object
# t = Structure.Trimester(" ", " "," "," "," ",)
#
#
# for key, values in currentDict.items():
#     if key == 'State':
#         s.State = values
#         print(key)
#         print(s.State)
#     elif key == 'VPH':
#         s.VPH = values
#         print(key)
#         print(s.VPH)
#     elif key == 'Spd':
#         s.Spd = values
#         print(key)
#         print(s.Spd)
#     elif key == 'Dir':
#         s.Dir = values
#         print(key)
#         print(s.Dir)
#     elif key == 'Location':
#         s.Location = values
#         print(key)
#         print(s.Location)
#     elif key == 'Occ':
#         s.Occ = values
#         print(key)
#         print(s.Occ)
#     elif key == 'Timestamp':
#         s.Timestamp = values
#         print(key)
#         print(s.Timestamp)
#     elif key == 'Station':
#         s.Station = values
#         print(key)
#         print(s.Station)
#     elif key == 'Interval':
#         s.Interval = values
#         print(key)
#         print(s.Interval)
#     elif key == 'Lanes':
#         s.Lanes = values
#         print(key)
#         print(s.Lanes)
#     elif key == 'IntId':
#         s.IntId = values
#         print(key)
#         print(s.IntId)
#     elif key == 'Cnt':
#         s.Cnt = values
#         print(key)
#         print(s.Cnt)
#
# print("completed the loop - exit program -0")



