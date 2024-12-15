
# '''Simple Inheritance'''
# class Car:
#     carName=''
#     def start(self):
#         print(self.carName,"Car Started")
#     def stop(self):
#         print(self.carName,"car stoped")
        
# class Toyota(Car):
#     def __init__(self,name) -> None:
#         Car.carName=name
        
# t1=Toyota("Fortuner")
# t1.start()
    
    
# '''MultiLevel Inheritance'''
# class Car:
#     carName=''
#     def start(self):
#         print(self.carName,"Car Started")
#     def stop(self):
#         print(self.carName,"car stoped")
        
# class Toyota(Car):
#     def __init__(self,name) -> None:
#         Car.carName=name
        
# class Fortuner(Toyota):
#     def __init__(self,type) -> None:
#         Car.type=type
        
# t1=Fortuner("Electric")
# t1.start()
    
'''Multiple Inheritance'''

class A:
    varA="class A"

class B:
    def varB(self):
        print( "Class B")

class C(A,B):
    varC="Class C"
    def __init__(self):
        super().varB()
        print(super().varA)
    # super().varB()

c1=C()
    
    