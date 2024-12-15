

'''Using self keyword, if we assign a value within a function it can be accesible within all other function also but not with function in the clas'''

# class students:
#     def __init__(self, fullname):
#         self.name=fullname
#         print(self.name)
#         self.greetings()
#         self.test()
    
#     def greetings(self):
#         self.name="lela"
#         print("Welcome Student",self.name)
     
#     def test(self):
#         print(self.name)

# s1=students("asdf")
# s1.greetings()
# s1.test()


# Question: create student class that takes marks and name of three subject as argument in constructor then create a method to print the average

class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        print(self.avg())
    def avg(self):
        avg=(self.m1+self.m2+self.m3)/3
        return self.name,avg
s1=student("hehe",50,21,33)


'''Static Methods'''
'''Its takes the methods changes it behaviour and return it'''
class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.age(20)
        print(self.avg())
        self.greetings()
        
    @staticmethod
    def greetings():
        print("welcome")
    
    def avg(self):
        avg=(self.m1+self.m2+self.m3)/3
        return self.name,avg
s1=student("hehe",50,21,33)
s2=student("hehe",50,21,33)
