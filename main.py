import FileNameReading, Parsing, Structure

filenames = FileNameReading.get_file_names()

saved = []

for i in filenames:
    data = Parsing.parse(i + '.csv')
    for row in data:
        saved.append(row)

# data = Parsing.parse('I-35S @ I-35 SB TO I 435 WB FF - First Trimester.csv')
for row in data:
    saved.append(row)

currentDict = {}
currentDict = saved[0]


s = Structure.StationData(" "," "," "," "," "," "," "," ") #figure out better NULL initialization of object
t = Structure.Trimester(" ", " "," "," "," ",)


for key, values in currentDict.items():
    if key == 'State':
        s.State = values
        print(key)
        print(s.State)
    elif key == 'VPH':
        s.VPH = values
        print(key)
        print(s.VPH)
    elif key == 'Spd':
        s.Spd = values
        print(key)
        print(s.Spd)
    elif key == 'Dir':
        s.Dir = values
        print(key)
        print(s.Dir)
    elif key == 'Location':
        s.Location = values
        print(key)
        print(s.Location)
    elif key == 'Occ':
        s.Occ = values
        print(key)
        print(s.Occ)
    elif key == 'Timestamp':
        s.Timestamp = values
        print(key)
        print(s.Timestamp)
    elif key == 'Station':
        s.Station = values
        print(key)
        print(s.Station)
    elif key == 'Interval':
        s.Interval = values
        print(key)
        print(s.Interval)
    elif key == 'Lanes':
        s.Lanes = values
        print(key)
        print(s.Lanes)
    elif key == 'IntId':
        s.IntId = values
        print(key)
        print(s.IntId)
    elif key == 'Cnt':
        s.Cnt = values
        print(key)
        print(s.Cnt)

s.Trimester1 = t

print(s.Trimester1.Location +  " here")


print("\nWhat can we do with the data, now that we have it stored\n")
print(s.Station)

print("We need to work with the numbers don't we?")

print("So the speed at time 0, on january 1st is " + s.Spd)

f = int(s.Spd) + 2

print(f)

