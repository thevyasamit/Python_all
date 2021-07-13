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


'''  

class Cars():
    b = 'Maruti'
    def setDetails(self, name ,year):
        self.n = name
        self.y =year    
    def getDetails(self):
        print(self.b,'--',self.n,'---',self.y)

o = Cars()
o.setDetails('Swift Dzire','2014')
o.getDetails()

# tata= Cars()
# tata.model_name = 'Harrier'
# tata.model_year = 2019
# tata.price = 1200000

# print(tata.model_name)
# print(type(tata))





