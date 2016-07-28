# definition of a structure where we might possible save the data? -> variables accessible, but then we would need to arrange them all in an order that would keep them sorted.

class StationData:
    def __init__(self, State, VPH, Spd,  Station, Interval, Lanes, IntId, Tri1):
        self.State = State #state is always empty for some reason... So it doesn't really make sense to even keep this field
        self.VPH = VPH
        self.Spd = Spd

        self.Station = Station
        self.Interval = Interval
        self.Lanes = Lanes
        self.IntId = IntId
        self.Trimester1 = Tri1


class Trimester: #These need to be lists? because it really won't work otherwise
    def __init__(self, Dir, Location, Occ, Timestamp, Cnt):
        pass
        self.Dir = Dir
        self.Location = Location
        self.Occ = Occ
        self.Timestamp = Timestamp
        self.Cnt = Cnt
        self.Counter = 0 # this counter will be used, to check how many times the object has been accessed
        #need to keep track of a list of files... 4 files top count fora trimester of data.. then linearly
        # need to have a way to know when to stop the count


# we want to restructure this to have a list, and be able to unite
# four files into one object? or something similar to that.


