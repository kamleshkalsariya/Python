class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

H = HashTable()
with open('nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])
        H[day] =temp
print(H['Jan-09'])
print(H['Jan-04'])



class complex_HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [{} for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h][key]

    def __setitem__(self, key,value):
        h = self.get_hash(key)
        found = False
        if (key in self.arr[h].keys()):
            self.arr[h][key] += value
            found = True
        if not found:
            self.arr[h][key] = 1

C =complex_HashTable()
with open('poem.txt','r') as f:
    for line in f:
        tokens = line.split()
        for item in tokens:
            C[item] = 1
for i in range(10):
    print(C.arr[i])
print(C['Two'])


#####

word_count = {}
with open("poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1
print(word_count)