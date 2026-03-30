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
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)

        if (self.minHeap and self.maxHeap and -self.maxHeap[0] > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val) 

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        
        return (-self.maxHeap[0] + self.minHeap[0])/2