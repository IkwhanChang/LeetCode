import heapq
import time

class LRUCache:
    cache = []
    size = 0
    def __init__(self, capacity: int):
        self.cache = []
        self.size = capacity
        

    def get(self, key: int) -> int:
        if len(self.cache) == 0:
            return -1
    
        
        if key in [k for t,k,v in self.cache]:
            for i,c in enumerate(self.cache):
                t,k,v = c
                if k == key:
                    t = time.time()
                    self.cache[i] = (t,k,v)
                    heapq.heapify(self.cache)
                    return v
            
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key not in [k for t,k,v in self.cache] and len(self.cache) == self.size:
            heapq.heappop(self.cache)
        
        found = False
        if key in [k for t,k,v in self.cache]:
            for i,c in enumerate(self.cache):
                t,k,v = c
                if k == key:
                    t = time.time()
                    self.cache[i] = (t,k,value)        
                    found = True
                    break
        if not found:   
            t = time.time()
            heapq.heappush(self.cache, (t, key, value))
        else:
            heapq.heapify(self.cache)
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)