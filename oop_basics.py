'''

We use class keyword for cretaing a class followed by the class name.
We use def to create a function in python.
-----------------------------------------------------

What are python modules?
The python files which have .py extension are called python modules. 
A module can have or define classes, functions, and variables.

--------------------------------------------

The mystery behind __name__ == __main__:
In python when the interpreter runs the code it always first sets some special variables and __name__ is one of them.
By default when an interpreter runs a module the __name__ is set to __main__ before a python code is run by the interpreter.
But if the program uses the imported module then __name__ variable will be set to the name of imported module.

-----------------------------------------------------

We can always use type() to know the type of the class whether it is inbuilt or user defined.
e.g. x = 1 print(type(x)) // it shows int class.

---------------------------------------------------------

We use self (anything in place of it) as it points to the current instance of the class. It is similar to 'this' used in java.


We use *args (it is not a keyword but has been used to keep things clear) when we don't know how many arguments
are being passed to function. It is also known as packing in python.
e.g. def summing(*args):
        argList = list(args)
        argList[0] = 10 # here we are trying to change the 1st element of the args
        argList[1] = 11 # here we are trying to change the 2nd element of the args which was something elese when we passed it from funciton call.
        return sum(args)
This function will return the sum of all the arguments we pass to it.
summing(1,2,4) # output will be 7
summing(1,2,3,5) # output will be 11
In this scenario the funciton summing() doesn't know the length of the parameter so we use packing in order to pack the variable 
length paramenters.

Anything declared inside __init__ (which is basically a constructor) comes under instance variable and the variables declar inside class will come under 
class variable i.e. accessed by all the class functions and members. 


'''  


# class Cars():
#     b = 'Maruti'
#     #setter method
#     def setDetails(self, name ,year):
#         self.n = name
#         self.y =year    
#     #getter method 
#     def getDetails(self):
#         print(self.b,'--',self.n,'---',self.y)
# #o is an object of type/class Cars. 
# o = Cars()
# o.setDetails('Swift Dzire','2014')
# o.getDetails()

# tata= Cars()
# tata.model_name = 'Harrier'
# tata.model_year = 2019
# tata.price = 1200000

# print(tata.model_name)
# print(type(tata))

# def funct(*argsList):
#     print('Trying to use the arg and kwarg argutments')
#     return sum(argsList)

# print(funct(3,5,3,2,2))


# #init is basically a contructor which we call. So when we use init we need to pass parameters while making object of the class. 
# #This can see the difference in cars (tata object creation) and students (stud object creation).

# class students():
#     def __init__(self,n, r, a):
#         self.name = n
#         self.age = a
#         self.rollno = r

#     def return_name(self):
#         return self.name
    
#     def return_roll(me):
#         return (me.rollno)



# if __name__ == "__main__":
#     stud = students('Jim', 34, 13)
#     #stud()
#     print("name is ", stud.return_name())


'''
OOP concepts are:   1. Inheritance  (i.e. child inheriting parent class)
                    2. Encapsulation (i.e. having private variables or functions)
                    3. Polymorphism  (i.e. one of the example could be one function used by 2 clases)
                    4. Data Abstraction (i.e. the modules we import are the best examples as they have code already in them)
'''

#  inheritance example in python. University is parent class and Eng is child classs extending University. 

class University:
    def __init__(self, name, location):
        self.uname = name
        self.ulocation = location
    
    def uniInfo(self):
        return f"University is : {self.uname} and location is {self.ulocation} \n"
    
class Eng(University):
    def __init__(self, name, location, cname):
        super().__init__(name, location)
        #
        self.cname = cname
        #we can also do University.__init__(self,name, location)
    def colInfo(self):
        return f"\nCollege is {self.cname} and university is {self.uname} and their location is {self.ulocation}\n"

obj1 = Eng('CSU', 'Cleveland', 'Washkiwiz')
print(obj1.colInfo())