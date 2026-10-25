class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        output = [0]*len(temperatures)

        while(temperatures):
            currentTemp = temperatures.pop()
            currIndex = len(temperatures) #fine since index is len-1

            daysDiff = 1
            while(len(monoStack) > 0 and monoStack[-1][0] <= currentTemp):
                temp = monoStack.pop()
                daysDiff += temp[1]
                
            if monoStack:
                output[currIndex] = daysDiff

            monoStack.append((currentTemp, daysDiff))

        return output