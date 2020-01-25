class Room:
    tag = 1
    def __init__(self, name, owner, width, length, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.height = height
    @property
    def cal_area(self):
        return ('%s 住的 %s 总面积是 %d' %(self.name,self.owner,self.width * self.length * self.height))
    def test(self):
        print('from test',self.name)
    # 类方法,相当于java的static方法：
    @classmethod
    def tell_info(cls,x):
        print(cls)
        print('---->+%s',x)
    # 工具包，既没有cls的类属性，也没有self的实例属性,因此不能调用类属性类方法，实例属性与实例方法
    @staticmethod
    def wash_body(a,b,c):
        print('%s %s %s正在洗澡' % (a,b,c))
    def test(x,y):
        print(x,y)
# r1 = Room("厕所",'alex',100,100,10000)
# print(r1.cal_area)
# print(r1.name)
# r1.test()
Room.tell_info('士大夫')
Room.wash_body('alex','yuanhao','wupeiqi')
Room.test(1,2)
r = Room("厕所",'alex',100,100,10000)
r.wash_body('alex','yuanhao','wupeiqi')
# r.test(1,2)
print(Room.__dict__)