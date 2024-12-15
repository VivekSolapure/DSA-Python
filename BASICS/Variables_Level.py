
'''Class-level Variable'''
class students:
    name="lela"  #works as static varibale i.e it gets 1 memory location; memory is not allocated on every object creation
    def gg(self, fullname):
        self.name=fullname
        self.__class__.name=fullname
        print(self.name)
        
    def test(self):
        print(self.__class__.name)
s1=students()
s2=students()
s1.gg("vivek solapure")
s1.test()
s2.test()


'''Using the @classmethod decorator for methods accessing class variables:'''
class Students:
    name = "lela"  # Class-level variable

    def __init__(self, fullname):
        self.name = fullname  # Instance-level variable
        print(self.name)

    @classmethod
    def print_class_name(cls):
        print(cls.name)  # Access class-level variable

s1 = Students("Vicky Souls")
Students.print_class_name()  # Print class-level variable via class method


'''Global'''

global_var = "I am global"

class Students:
    def __init__(self, fullname):
        self.name = fullname
        print(global_var)  # Can access global variable

s1 = Students("Vicky Souls")


'''Nonlocal Variables (in nested functions)'''

def outer_function():
    x = "outer variable"

    def inner_function():
        nonlocal x  # Refers to the 'x' in the outer_function
        x = "modified by inner"
        print(x)

    inner_function()
    print(x)

outer_function()
