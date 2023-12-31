

class Bucket:
    
    def __init__(self) -> None:
        self.bucket = []


    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1


    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                found = True
                self.bucket[i] = (key, value)
                break
        
        if not found:
            self.bucket.append((key, value))


    def delete(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class HashMap:

    def __init__(self) -> None:
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]


    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def put(self, key, value):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].update(key, value)

    def remove(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].delete(key)        


obj = HashMap()
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
obj.put(1, 1)
obj.put(2, 2)
res1 = obj.get(1)
res2 = obj.get(3)

print(res1)
print(res2)

param_2 = obj.get(1)
print(param_2)
obj.remove(1)


