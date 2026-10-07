
#1) oop- object oriented programming
#it is a programming approach where we organize our program around objects rather than only functions and variables.
#student:
#data:
#- name,age,marks,roll_no
#- study(), attend_classes(), write_exam(),
#in oops, we combine data+behaviour into object

#2) class:
#blue print or template to create objects

#3) object:
#instances of class

# class student:
#     pass
# student1=student()  #student -> object
# student2=student()

#4) attributes"
#Attributes are the data or propertites associated with an object.
# class student:
#     pass
# student1=student()
# student1.name="vivek"
# student1.age=22
# student1.marks=98
# print(student1.name)
# print(student1.age)
# print(student1.marks)

#methods
#methods- functions created inside class

# class student:
#     def study(self):
#         print("student is studying")
# student1=student()
# student1.study()
#methods only belongs to class

#constructor
# constructor - it is a special method that is automatically called when an object is created.
#__init__()
# class Student:
#     def study(self):
#         print("student is studying")
# student1=Student()  

#constructor with attributes
# class Student:
#     def __init__(self, name, age, marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
# student1=Student("vivek",22,95)
# print(student1.name)
# print(student1.age)
# print(student1.marks)   
#self represents current object.


#creating class and objects with multiple methods
# class Student:
#     def __init__(self, name, age, marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name, self.age, self.marks)    
# student1=Student("vivek",22,95)
# student1.display()

#encapsulation:
#encapsulation - means bundling data and methods together inside a class and controlling how that data is accessed or modified.
# class BankAccount:
#     def __init__(self, balance):
#         self.balance=balance
#     def deposit(self, amount):
#         self.balance+=amount
#     def withdraw(self, amount):
#         self.balance-=amount 
#     def get_balance(self):
#         return self.balance
# ba = BankAccount(50000) 
# ba.deposit(10000)
# ba.withdraw(5000)
# print(ba.get_balance()) 
#double underscore indicates a private-like attribute in python through name managing


#getter and setter concept
#private data
#getter -> read data
#setter -> modify data safely

# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self, marks):
#         if 0<=marks <=100:
#             self.__marks = marks
#         else:
#             print("invalid marks")
# student = Student(80)
# print(student.get_marks())
# student.set_marks(90)
#  print(student.get_marks())

# inheritance:
# process of acquirng properties from parent class to child class
# types of inheritance:
# 1) single inheritance
#  one parent -> one child
# #parent class
# class animal:
#     def eat(self):
#         print("animal eats")
# child class  
# class lion(animal):
#      def roar(self):
#         print("lion roars")
# l = lion()
# l.eat()
# l.roar()

# #2) multiple inheritance
# #one child inherits from multiple parents
# class Father:
#     def father_properties(self):
#         print("father properties")
# class Mother:
#     def mother_properties(self):
#         print("mother properties")
# # child class
# class Child(Father, Mother):
#   def child_properties(self):
#       print("child properties")
# c = Child()
# c.father_properties() 
# c.mother_properties()
# c.child_properties()    

# #3) multilevel inheritance
# #inheritance happens across multiple levels
# #grandparent -> parent -> child
# class Grandparent:
#     def house(self):
#         print("grandparent's house")
# class Parent(Grandparent):
#     def car(self):
#         print("parent's car")
# class Child(Parent):
#     def bike(self):
#         print("child's bike")
# c = Child()
# c.house()
# c.car()
# c.bike() 

# #4) hierarchical inheritance
# #one parent -> multiple children
# class animal:
#     def eat(self):
#         print("animal eats")
# #child class 1
# class Dog(animal):
#     def bark(self):
#         print("dog barks")
# #child class 2
# class Cat(animal):
#     def meow(self):
#         print("cat meows")
# d = Dog()
# c= Cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()

# #5) hybrid inheritance
# #combination of two or more types of inheritance
# class A:
#     def method_a(self):
#         print("method A")
# class B(A):
#     def method_b(self):
#         print("method B")
# class C(A):
#     def method_c(self):
#         print("method C")
# class D(B, C):
#     def method_d(self):
#         print("method D")   
# obj = D()
# obj.method_a()
# obj.method_b()
# obj.method_c()
# obj.method_d()

#super method
#in python, super() is used to access functionality from the parent class.
# class Parent:
#     def show(self):
#         print("parent method")
# class Child(Parent):
#     def show(self):
#         super().show()  #calling parent method
#         print("child method")
# c = Child()
# c.show()  

#super() with constructor
# class Person:
#     def __init__(self, name):
#         self.name = name
# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks
# s = Student("Vivek", 95)
# print(s.name)
# print(s.marks)

# vehicle and car example problem
#vehicle -> car
#vehicle - start(), stop()
#car -  drive
# class Vehicle:
#     def start(self):
#         print("vehicle start")
#     def stop(self):
#         print("vehicle stop")
# class Car(Vehicle):
#     def drive(self):
#         print("car is driving")
# c = Car()
# c.start()
# c.stop()
# c.drive()

#person and student example problem
#person -> student
#person - name, age, dispplay_person()
#student - roll_no, course, display_student()
#output:
#name, age, roll_no, course
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_person(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# class student(person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course
#     def display_student(self):
#         self.display_person()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)
# s = student("Vivek", 22, "521411088", "CsE")
# s.display_student()
      
    
#polymorphism
#polymorphism - one name, many forms
#poly - many
#morphism - forms
#in python, polymorphism means the same method, function, or operator can behave differently depending on the object or data being used.
# class Dog:
#     def sound(self):
#         print("Dog barks")
# class Cat:
#     def sound(self):
#         print("Cat meows")
# d = Dog()
# c = Cat()
# d.sound()  
# c.sound() 

#types of polymorphism:
#1) method overloading
#2) method overriding
#3) operator overloading

#1) method overriding - same method name but different implementation in child class.
#it occurs when a child class provides its own implementation of a method that is already exists in parent class.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# d = Dog()
# c = Cat()
# d.sound()  
# c.sound()

#2) method overloading
# having multiple methods with the same name but different parameters
# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def add(self, a, b, c):
#         return a + b + c
# calc = Calculator()
# print(calc.add(5, 10))
# print(calc.add(5, 10, 15))

#1) default arguments
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
# calc = Calculator()
# print(calc.add(5, 10)) #a, b machine c=0 automatically
# print(calc.add(5, 10, 15))

#2) using *args
# class Calc:
#     def add(self, *args):
#         return sum(args)
# c=Calc()
# print(c.add(5, 10))
# print(c.add(5, 10, 15))
# print(c.add(5, 10, 15, 20, 25)) 
# print(c.add(5, 10, 15, 20, 25, 30, 35)) 

#difference between method overloading and method overriding:
# features                      overloading                             overriding
#1) classes                     same class                              parent and child class
#2) method name                 same                                    same
#3) parameters                  different                               same
#4) purpose                     different ways of calling a method      changing parent behavior
#5)python support               not directly supported                  supported
#6)example                      add(a,b), add(a,b,c)                    animal.sound() -> Dog.sound(), Cat.sound()


#operator polymorphism
#operator overloading - same operator behaves differently based on the operands.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
# p1 = Point(10, 20)
# p2 = Point(30, 40)
# p3 = p1 + p2
# print(p3.x, p3.y)  # Output: 40 60

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def __eq__(self, other):
#         return self.marks == other.marks
# s1 = Student("Vivek", 95)
# s2 = Student("Akash", 95)
# print(s1 == s2)  # Output: True


#absraction
#abstraction - hiding the implementation details and showing only the essential features of an object.
# from abc import ABC, abstractmethod
# #ABC called as abstract base class
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# #animal says that every animal must provide a sound() method
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog = Dog()
# cat = Cat()
# dog.sound()  
# cat.sound()         

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
class CreditCard(payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
upi = UPI()
card = CreditCard()
upi.pay(5000)
card.pay(10000)
        