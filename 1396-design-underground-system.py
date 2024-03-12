class UndergroundSystem:

    def __init__(self):
        self.custmap = {}
        self.station_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.custmap[id] = {"start": t, "station": stationName}
        if not stationName in self.station_map:
            self.station_map[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        travel_obj = self.custmap[id]
        start_st = travel_obj["station"]
        start_t = travel_obj["start"]
        time = t - start_t
        del self.custmap[id]

        if stationName not in self.station_map[start_st]:
            self.station_map[start_st][stationName] = [time]
        else:
            self.station_map[start_st][stationName].append(time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.station_map[startStation][endStation]
        return sum(times)/len(times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
