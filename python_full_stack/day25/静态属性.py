class Room:
    def __init__(self, name, owner, width, length, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.height = height
    @property
    def cal_area(self):
        return ('%s 住的 %s 总面积是 %d' %(self.name,self.owner,self.width * self.length * self.height))
    
r1 = Room("厕所",'alex',100,100,10000)
print(r1.cal_area)
