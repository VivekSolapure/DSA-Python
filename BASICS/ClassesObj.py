# class person:
#     name='vicky'
#     surname='sol'
#     def fun(self):
#         print(self.name)
# a=person()
# b=person()
# b.name="vivek"
# a.fun()
# b.fun()
''' When the object is created blueprint will be assigned a memory and it will become real
    ->firstly we were using procedural porgramming which excutes line by line 
    ->then we jumped to function for REDUCING REDUNDANCY and INCREASING RESUSABLITY 
    ->Then we jumped to objects and classes to mainly increase RESUSABLITY
'''
class person:
    def fun(sel):
        sel.name="vv"
        print(sel.name)
    def fog(self):
        self.name="aa"
        print(self.name)
        # print(self)
a=person()
b=person()
b.name="vivek"
a.fun()
a.fog()
# b.fun()