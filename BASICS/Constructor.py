""" CONSTRUCTOR """
''' Constructor are created even if we not create it by the class
    It always include the self parameter 
    It will be automatically called whenever we create object of the class(In all languages)
    'self' keyword simply points to the object we are creating to the class i.e self is the reference(memory locations pointer) of the object
    'self' is also used to access class level variables 
    ->TYPES
        -Default  def __init__(self).... Created weven if we not create it
        -Parameterized   def __init__(self,name,marks) 
'''

class students:
    name="lela"
    def __init__(self, fullname):
        self.name=fullname
        print(self.name)  #This will print "Vicky Souls" bcz obj attribute has higher precedence than class attr 
        print(self.__class__.name)
        print(self.name)
    def fun(self):
        print(self.name)
        
        
s1=students("Vicky Souls")
s1.fun() 

arr=[1,2,3,4,5]
print()
my_dict = {i:i+7 for i in range(1, 10)}
print(my_dict)
