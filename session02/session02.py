import os
from urllib.parse import ParseResultBytes
os.system('cls' if os.name == 'nt' else 'clear')

# def print_type(data):
#     for i in data:
#         print(i, type(i))

# test = [123, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x, {"name": "Barry"}]

# print_type(test)

# class Person:
#     name = 'Barry'
#     age = 44

# person1 = Person()
# person2 = Person()

###! Class Attributes vs Instance Attributes

# person1.name = 'Halil'
# person1.job = 'teacher'

# Person.name = 'Fatih'
# Person.age = 29

# print(person1.name, person2.age)
# print(person2.name, person2.age)

###! SELF keyword

# class Person:
#     name = 'Barry'
#     age = 44

#     def test(self):
#         print('test')

#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     def get_details(self):
#         print(f"name : {self.name}   age: {self.age}   location: {self.location}")
    
#     @staticmethod
#     def salute():
#         print('Hi There')

# person1 = Person()
# # person1.test()
# # Person.test(person1)

# # person1.set_details('Fatih',29, 'Germany')
# # person1.get_details()

# Person.salute()

# special methods

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name : {self.name}   age: {self.age}" 

#     def __len__(self):
#         return self.age

#     def get_details(self):
#         print(f"name : {self.name}   age: {self.age}")    


# person1 = Person('Barry', 44)
# person1.get_details()

# lst = [1,2,3,4,5]
# print(lst)
# print(person1) # person1.__str__()

# print(len(lst))
# print(len(person1))

###! encapsulation and abstraction (sarmalama/soyutlama)

###! istedigimiz bilgileri örnegin id gibi unic degerleri saklayabiliriz
###! 
###! 
###! 

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id2 = 4000

#     def __str__(self):
#         return f"name : {self.name}   age: {self.age}" 

#     def set_details(self):
#         print(f"name : {self.name}   age: {self.age}")  
#   
#     def get_details(self):
#         print(f"name : {self.name}   age: {self.age}")    

# person1 = Person('Barry', 44)
# print(person1._id)
# # print(person1.__id2)
# print(person1._Person__id2)

# lst = [2,9,1,6]
# lst.sort()
# print(lst)

###! inheritance and polymorphism

###! kalıp olusturdugumuz classtan türettigimiz classlara inheritance yapılır 
###! fakat biz bazı fonksiyon veya methodları farklı kullanmak istersek 
###! burada polymorphism ile overwrite/overload vb methodlarla degisiklik yapabiliriz(yani esneklik vardır) 

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name : {self.name}   age: {self.age}" 

#     def get_details(self):
#         print(f"name : {self.name}   age: {self.age}")  

# class Lang():
#     def __init__(self,langs):
#         self.langs = langs

# class Employee(Person, Lang):
#     def __init__(self, name, age, path, langs):
#         # self.name = name
#         # self.age = age
#         super().__init__(name,age)
#         Lang.__init__(self,langs)
#         self.path = path
    
#     # override
#     def get_details(self):
#         super().get_details()
#         print(f"name : {self.name}   age: {self.age}   path: {self.path}   langs: {self.langs}") 

    

# emp1 = Employee('Barry',44,'FS',['Pyhton','JS'])
# emp1.get_details()

# print(Employee.mro())

# inner class

# from django.db import models

# class Article(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['first_name']
#         model = Customer

# class Person:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#         self.movements = []

#     def add_movement(self, amount, date, explain):
#         self.movements.append({"amount":amount, 'date': date, 'explain': explain})

#     def all_movements(self):
#         # print(self.movements)
#         for i in self.movements:
#             print(i["date"], i["amount"], i['explain'])

#     def balance(self):
#         # sum = 0
#         # for i in self.movements:
#         #     sum += i['amount']
#         # return sum
#         return sum([i['amount'] for i in self.movements])

# person1 = Person('barry',44)
# person1.add_movement(1000,'26.04.2022','salary')
# person1.add_movement(-500,'26.04.2022','rent')
# person1.add_movement(-300,'26.04.2022','bill')
# person1.add_movement(500,'26.04.2022','free lance')
# person1.add_movement(-600,'26.04.2022','market')

# person1.all_movements()
# print(person1.balance())

# def twoSum(nums, target):
#     return [[i,j] for i in range(len(nums)) for j in range(i+1,len(nums)) if nums[i] + nums[j] == target][0]

# print(twoSum([3,5,7],8))
