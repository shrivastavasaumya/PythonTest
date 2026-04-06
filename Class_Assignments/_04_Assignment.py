
class BankAccount:
    def  __init__(self, name, __balance, number):
        self.name = name
        self.__balance = __balance
        self.number = number
                                                #Q1
    def getbalance(self):
        return self.__balance
    
    def deposit(self, depositAmt):
        self.__balance += depositAmt
        print("total balance",self.__balance)
        return
    
    def withdraw(self, amtwithdraw):
        if amtwithdraw >= self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amtwithdraw
            print("updated balance", self.__balance)
        return

    def show_history(self):
        print("\n Transaction History:")
        for transaction in self.history:
            print(transaction)


acc1 = BankAccount("Dua" , 4000, 45876)
print(acc1.getbalance())
acc1.deposit(500)
acc1.withdraw(4500)
acc1.withdraw(100)

#--------------------------------------------------------------------

class Book:
    def __init__(self, Title, Author, list_of_reviews):             #Q2
        self.Title = Title
        self.Author = Author
        self.list_of_reviews = list_of_reviews
        self.history = []
    
    def new_review(self , adding_new_review):
        self.list_of_reviews.append(adding_new_review)
        self.history.append(adding_new_review)
        print("Review added!")

    def count(self ):
        return len(self.list_of_reviews)
        
    
    def display_all(self):
        print("\n All reviews:")
        for l in self.list_of_reviews:
            print(l)


Book1 = Book("Animal Farm" , "George Orwell", ["wow!", "Fab!", "Awesome!" ])
Book1.display_all()
Book1.new_review("Great book!")
Book1.display_all()    
print(Book1.count())


#| Function type | Behavior                                  |
#| ------------- | ----------------------------------------- |
#| `print()`     | shows output on screen                    |
#| `return`      | sends value back (but doesn’t display it) |

#---------------------------------------------------------------------

# class Student:
#     def __init__(self, name, rollNo, marks):
#         self._name(name)
#         self._roll_no(rollNo)
#         self._marks(marks)

    
#     def get_name(self):
#         return self.__name
    
#     def get_rollNo(self):
#         return self.__roll_no                                                                                     # Error code
    
#     def get_marks(self):
#         return self.__marks
    
#     def set_name(self, name):
#         if name.strip() == "":       # strip() removes whitespaces from the string
#             print("Name cannot be empty")
#         else:
#             self.__name = name

#     def set_rollNo(self, rollNo):
#         if 1 <= rollNo <= 100:
#             self.__roll_no = rollNo
#         else:
#             print("Roll number must be between 1 and 100")

#     def set_marks(self, marks):
#         if marks >= 0:
#             self.__marks = marks
#         else:
#             print("Marks cannot be negative")


# Student1 = Student( '', 24, 85)
# print(Student1.get_marks())
# print(Student1.get_rollNo())
# print(Student1.get_name())

class Shape:
    def area(self):
        pass
                                                                                     #Q4                                                                                    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Objects
c = Circle(5)
r = Rectangle(8, 9)
t = Triangle(6, 4)

print("Area of Circle =", c.area())
print("Area of Rectangle =", r.area())
print("Area of Triangle =", t.area())

#-----------------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
       
                                                                    #Q5
class car(Vehicle):
    def __init__(self,brand , model, seats):
        super().__init__(brand , model)
        self.seats = seats
        

class bike(Vehicle):
    def __init__(self,brand , model, engine_cc):
        super().__init__(brand , model)
        self.engine_cc = engine_cc
        
    
Car1 = car("Honda", "city", 7)
print(Car1.brand, Car1.seats, Car1.model)

#------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
                                                                  #Q6
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(employee):
    def calculate_salary(self):
        print("10000")

class FullTimeEmployee(employee):
    def calculate_salary(self):
        print("40000")

class ContractEmployee(employee):
    def calculate_salary(self):
        print("20000")

Intern = Intern()
Intern.calculate_salary()

#---------------------------------------------------------------------------------------------------------
class person:
    def __init__(self , name, age = 0, address =0):
        self.name = name
        self.age = age
        self.address = address
                                                                            #Q7
person1 = person("kappa", "85", "Gokul")
print(person1.name)
print(person1.name, person1.age)
print(person1.name, person1.age, person1.address)

#----------------------------------------------------------------------------------------------------------

class player:
    player_count = 0
                                                                                    #Q8
    def __init__(self, name, level):
        self.name = name
        self.level = level
        player.player_count += 1
    

p1 = player("Virat", 14)
p2 = player("Rohit", 15)
p3 = player("Dhoni", 18)
p4 = player("Suryakumar", 14)

print(player.player_count)

#-------------------------------------------------------------------------------------------------------------------


class Herbivore:
    def __init__(self, plants):
        self.plants = plants

    def eat_plants(self):
        print(f"Eats plants: {self.plants}")
                                                                                     #Q9

class Carnivore:
    def __init__(self, meat):
        self.meat = meat

    def eat_meat(self):
        print(f"Eats meat: {self.meat}")


class Omnivore:
    def __init__(self, food):
        self.food = food

    def eat_all(self):
        print(f"Eats everything: {self.food}")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, plants, meat, food):
        Herbivore.__init__(self, plants)
        Carnivore.__init__(self, meat)
        Omnivore.__init__(self, food)

    def show_diet(self):
        print("Bear diet:")
        self.eat_plants()
        self.eat_meat()
        self.eat_all()


# Create object
b1 = Bear("grass", "fish", "berries")

b1.show_diet()

#-----------------------------------------------------------------------------------------------------

