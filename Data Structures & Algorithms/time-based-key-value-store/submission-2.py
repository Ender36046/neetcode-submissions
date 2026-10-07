class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pairing = (value, timestamp)
        if(self.hashmap.get(key,0) != 0):
            self.hashmap[key].append(pairing)
        else:
            self.hashmap[key] = [pairing]

    def get(self, key: str, timestamp: int) -> str:
        if(self.hashmap.get(key,0) == 0):
            return ""
        listOfPairs = self.hashmap[key]
        if(listOfPairs[0][1] > timestamp):
            return ""
        l,r = 0,len(listOfPairs)-1
        bestPair = 0
        while(l <= r):
            middle = (l+r)//2
            if(listOfPairs[middle][1] > timestamp):
                r = middle-1
            elif(listOfPairs[middle][1] < timestamp):
                bestPair = middle
                l = middle +1
            elif(listOfPairs[middle][1] == timestamp):
                return listOfPairs[middle][0]
        return listOfPairs[bestPair][0]
            