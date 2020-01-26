class Hand:
    pass
class Foot:
    pass
class Trunk:
    pass
class Head:
    pass
class Person:
    def __init__(self,id_num,name):
        self.id_num = id_num
        self.name = name
        self.hand = Hand()
        self.foot = Foot()
        self.trunk = Trunk()
        self.head = Head()
p1 = Person('1111','alex')
print(p1.__dict__)



class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
class Cource:
    def __init__(self,name,price,period,school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school
s1 = School('oldboy','北京')
s2 = School('oldboy','南京')

c1 = Cource('linux',10,'1h',s1)
print(c1.__dict__)
print("end")