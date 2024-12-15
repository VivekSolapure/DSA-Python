'''
    private variable: Syntax  "__variable name", accessible only inside the class
    private methods: Syntax  "__method name", accessible only inside the class
'''

class student:
    __name="vivek"
    def __init__(self) -> None:
        self.getname()
        self.__grettings()
    
    def getname(self):
        return self.__name
    
    def __grettings(self):
        print("hello",self.getname())

s1=student()
# print(s1.__name)