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
