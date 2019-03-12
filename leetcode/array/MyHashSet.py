class MyHashSet(object):

    def __int__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]
    def contains(self,key):
        _, idx = self._index(key)
        return idx > 0
    def add(self,key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)
    def remove(self,key):
        bucket,idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)
    def _hash(self,key):
        return key % self.size
    def _index(self,key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i,k in enumerate(bucket):
            if key == k:
                return bucket,i
        return bucket,-1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)