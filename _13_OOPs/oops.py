class Student:
    college_name = "ABC college"   #class
    
    def __init__(self, name, gpa):
        self.name = name           #instance
        self.gpa = gpa

stu1 = Student("Rahul", 9.2 )
print(stu1.name)   # to access/invoke instance attributes we have to write object's name 

# print(Student.name)   # what if we use 'class' name -----> ERROR cause 'Student' class doesn't have any 'name' attribute


print(Student.college_name)    # 'class' attributes can be called from 'class names as well as object names' 
print(stu1.college_name)   # [both are correct]


# what if both the 'class' and 'instance' have same attribute = the 'instance value' will get printed as it is prioritised 
# cause 'instance' has unique value and 'class' has same value/common value

class laptop:
    storage_type = 'ssd'

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.srorage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM and {self.srorage} {self.storage_type}")

    @staticmethod
    def cal_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

l1 = laptop('16gb', '512gb')
l2 = laptop('8gb', '256gb')

l1.cal_discount(40_000, 10)



class product:
    count = 0 # common for all objects so it should be inside a class variable/attribute
    
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        product.count += 1    # to know about the creation of new  objects, we need to put it in the constructor
                              # 'product' cause we are making count under 'product class'
                              # instead if we use 'self.count'  a new variable will be formed with the name 'count' wchich will only
                              # access the 'instances' not the 'class' so to count both we used 'product.count'
   
    def get_info(self): # instance method
        print(f"The price of {self.product_name}is Rs. {self.price}")

    @staticmethod
    def cal_discount( price, a):
        final_price = price - (a * price / 100)
        print(f"discounted price is = {final_price}")  
    
    @classmethod
    def get_count(cls):
        print(f"Total products = {cls.count}")

p1 = product("Phone", 12000)
p2 = product("Laptop", 55000)
p3 = product("TV", 25000)



product.get_count()
p1.cal_discount(p1.price, 12)



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
        
#         self.__balance = balance   # private

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, newBlance):
#         self.__balance = newBlance
        


# acc1 = BankAccount("Rahul Kumar", 100000)
# acc1.set_balance(2000000)
# print(acc1.name, acc1.get_balance())      # Rahul Kumar 100000



class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        
        self.__balance = balance   # private
        


acc1 = BankAccount("Rahul Kumar", 100000)

print(acc1.name, acc1._BankAccount__balance)      # Rahul Kumar 100000

#___________________________________________________________________________________
#Multi-line inheritance

class employee:
    start_time = '10 am'
    end_time = '6 pm'

class staff(employee):
    def __init__(self, role):
        self.role = role

class accountant(staff):
    def __init__(self,  salary, role) :
        super().__init__(role)  # to run this we have to fulfill the requirements of the prior function cause of the Multi-level inheritance 
        self.salary = salary #                for that use -> 'super()' calls/invoke the superior class or parent class constructor 1st

acc1 = accountant(100000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

#_____________________________________________________________________
# multiple inheritance

class teacher:
    def __init__(self, salary):
        self.salary = salary

class student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(teacher, student):
    def __init__(self, salary, gpa, name):
        super().__init__( salary) # don't need to pass 'self' in directly calling with'super' [for 1st parent call]
        student.__init__(self,gpa) # don't need to pass 'super' for 2nd parent call cause when we call via class name we need to use object reference that is 'self'
        self.name = name

ta1 = TA(15_000, 9.3, "Pawan")

print(ta1.name, ta1.gpa, ta1.salary)       
        



from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod       # ----> abstractmethod by default does not have implementation in parent/original class, this are those methods whose 
    def make_sound(self): #       implementation is only after inheritance in the child class 
        pass

class Lion(Animal):
    def make_sound(self):
            print("Roar!")

class Cow(Animal):
    def make_sound(self):
            print("Moo!")
        
cow = Cow()
cow.make_sound()

lion = Lion()
lion.make_sound()


# Polymorphism(over-riding)

class Employee:
    def get_designation(self):    # a parent-class function
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):     # over-riding it again in child class
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

# designation = Teacher

#__________________________________________________
# Duck-typing

class Accountant:
    def get_designation(self):    # a seperate class
        print("designation = Accountant")

class Teacher:
    def get_designation(self):     # other class
        print("designation = Teacher")
                                   # but the work of function 'get_designation' is same = duck typing = so same name in both classes
t1 = Teacher()
t1.get_designation()
# designation = Teacher

t1 = Accountant()
t1.get_designation()
# designation = Accountant

