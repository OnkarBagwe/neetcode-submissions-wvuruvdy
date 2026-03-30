class RandomizedSet:

    # def __init__(self):
    #     self.randomMap = {}
    #     self.randomList = []     

    # def insert(self, val: int) -> bool:
    #     if val in self.randomMap:
    #         return False
    #     else:
    #         self.randomMap[val] = len(self.randomList)
    #         self.randomList.append(val)
    #     return True

    # def remove(self, val: int) -> bool:
    #     if val not in self.randomMap:
    #         return False
    #     else:
    #         idx = self.randomMap[val]
    #         lastVal = self.randomList[-1]
    #         self.randomList[idx] = lastVal
    #         self.randomList.pop()
    #         self.randomMap[lastVal] = idx
    #         del self.randomMap[val]
    #     return True

        
    # def getRandom(self) -> int:
    #     return random.choice(self.randomList)
    def __init__(self):
        self.randomMap = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        if val not in self.randomMap:
            self.randomMap[val] = len(self.randomList)
            self.randomList.append(val)
        else:
            return False
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomMap:
            return False
        else:
            lastVal = self.randomList[-1]
            idx = self.randomMap[val]
            self.randomList[idx] = lastVal
            self.randomList.pop()
            self.randomMap[lastVal] = idx
            del self.randomMap[val]
        
    def getRandom(self) -> int:
        return random.choice(self.randomList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()