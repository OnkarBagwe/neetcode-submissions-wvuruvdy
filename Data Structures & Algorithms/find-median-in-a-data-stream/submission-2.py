class MedianFinder:

    # def __init__(self):
    #     self.data = []

    # def addNum(self, num: int) -> None:
    #     self.data.append(num)

    # def findMedian(self) -> float:
    #     self.data.sort()

    #     n = len(self.data)
    #     if n%2 == 0:
    #         return ((self.data[n//2] + self.data[(n//2)-1])/2)
    #     else:
    #         return self.data[n//2]

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        #make sure every element in small <= every element in large
        if(self.small and self.large and -self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0]+self.large[0])/2
