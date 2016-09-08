import FileNameReading, Parsing, Structure, Functions, Clean

# dictionary that contains all the filenames
filenames = FileNameReading.get_file_names()

all_sensors = []

for i in filenames.keys():
    current_sensor = []
    data = Parsing.parse(i)
    print("Current file being read is " + i)
    data = Clean.remove_empty(data)
    for row in data:
        current_sensor.append(row)
    all_sensors.append(current_sensor)

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



