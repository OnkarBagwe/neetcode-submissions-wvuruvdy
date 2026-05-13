# class MyHashMap:

#     def __init__(self):
#         self.hashMap = [-1] * 1000001

#     def put(self, key: int, value: int) -> None:
#         self.hashMap[key] = value

#     def get(self, key: int) -> int:
#         return self.hashMap[key]

#     def remove(self, key: int) -> None:
#         self.hashMap[key] = -1

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key%len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        curr = self.hashmap[self.hash(key)].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashmap[self.hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return            
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)