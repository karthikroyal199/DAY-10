

# ? Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")


i = IOB()
i.ratio()

s = SBI()
s.ratio()




# ? Eg:2
class USA:
    def langauge(self):
        print("English")

    def capital(self):
        print("Washington DC")

class india(USA):
    def langauge(self):
        print("None")
        
def capital(self):
    print("New delhi")


I = india()
I.langauge()
I.capital()



# ? Eg:3

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

 obj1 = c2():
 obj.f1()
 
def display


# --> method over riding
# ploymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")

class sbi(bank):
    def ratio(self):
        print("sbi rate is 9%")

class iob(bank):
    def ratio(self):
        print("iob rate is 7.5%")

i=iob()
i.ratio()

s=sbi()
s.ratio()

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()



# -->Method overloading
# Eg:1

class suming:
    def add(self, a, b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)


s=suming()
#s.add(4,3) # ----> error
s.add(4,5,1)




# Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)




# ----> Abstraction

class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
       
tr triangle()
tr.traingle_sides()
tr.name()

# * Eg_3:-
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd
    

class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)





# Eg:1

class car:
    _name = "BMW" # Private variable
    print(_name)
    
 c1 = car()
 print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error


# * ----> Accessing private data outside the class
class c1:
    __phone = '7656567687'
    
    def display(self):
        print(self.__phone)
c = c1()
c.display()



# *-----> Eg:3
# ? declare private method
class class1:
    def __m1(self):
        print("Iam private method")

    def __init__(self):
        self._m1()
c = class1()
c._m1() # error


# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)

    obj1 = class2()

obj = class1()
obj.obj1.display()


d1 = ("shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30
for val in d1:
if d1 [val] = min(d1.values());
print(val)
for val in d1:
if d1 [val] max(d1.values()):
print(val)
for val in d1:
if val.startswith('s') or val.startswith('S'): print(val)c
ssv-hcbt-rgo

# --> method over riding
# ploymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")

class sbi(bank):
    def ratio(self):
        print("sbi rate is 9%")

class iob(bank):
    def ratio(self):
        print("iob rate is 7.5%")

i=iob()
i.ratio()

s=sbi()
s.ratio()

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()



# -->Method overloading
# Eg:1

class suming:
    def add(self, a, b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)


s=suming()
#s.add(4,3) # ----> error
s.add(4,5,1)




# Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)




# ----> Abstraction

class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
       
tr triangle()
tr.traingle_sides()
tr.name()

# * Eg_3:-
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd
    

class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)





# Eg:1

class car:
    _name = "BMW" # Private variable
    print(_name)
    
 c1 = car()
 print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error


# * ----> Accessing private data outside the class
class c1:
    __phone = '7656567687'
    
    def display(self):
        print(self.__phone)
c = c1()
c.display()



# *-----> Eg:3
# ? declare private method
class class1:
    def __m1(self):
        print("Iam private method")

    def __init__(self):
        self._m1()
c = class1()
c._m1() # error


# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)

    obj1 = class2()

obj = class1()
obj.obj1.display()


d1 = ("shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30
for val in d1:
if d1 [val] = min(d1.values());
print(val)
for val in d1:
if d1 [val] max(d1.values()):
print(val)
for val in d1:
if val.startswith('s') or val.startswith('S'): print(val)c
ssv-hcbt-rgo


























