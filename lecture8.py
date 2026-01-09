# Object Oriented Programming in Python
# This script demonstrates the basics of Object Oriented Programming (OOP) in Python.
# It covers the concepts of classes, objects, attributes, and methods.

# Class - A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
class Student :
    name = ""  # Attribute to store the name of the student
    age = 0    # Attribute to store the age of the student
    def greet(self) :  # Method to greet
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

# Object - An instance of a class. It is created using the class blueprint.
student1 = Student()  # Creating an object of the Student class
student1.name = "Alice"  # Setting the name attribute
student1.age = 20        # Setting the age attribute
student1.greet()        # Calling the greet method



# Constructor - A special method that is called when an object is instantiated. It is used to initialize the attributes of the object.
class Car :
    # default constructor
    def __init__(self) :
        print("A new car object has been created.")
    # parameterized constructor
    def __init__(self, make, model, year) :  # Constructor with parameters
        print(self) # Print the instance reference
        self.make = make    # Attribute to store the make of the car
        self.model = model  # Attribute to store the model of the car
        self.year = year    # Attribute to store the year of the car
    def display_info(self) :  # Method to display car information
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

car1 = Car("Toyota", "Camry", 2020)  # Creating an object of the Car class
print(car1.model)  # Accessing the model attribute
car1.display_info()  # Calling the display_info method



# Class & Instance attribute
class Student1 :
    school = "ABC High School"  # Class attribute
    def __init__(self, name, age) :
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    def display(self) :
        print(f"Name: {self.name}, Age: {self.age}, School: {Student1.school}")

student2 = Student1("Bob", 18)  # Creating an object of the Student1 class
student2.display()  # Calling the display method    



# Methods - Functions defined inside a class that operate on the attributes of the class.
class Rectangle :
    def __init__(self, length, width) :
        self.length = length  # Attribute to store the length of the rectangle
        self.width = width    # Attribute to store the width of the rectangle
    def area(self) :  # Method to calculate area
        return self.length * self.width
    def perimeter(self) :  # Method to calculate perimeter
        return 2 * (self.length + self.width)
    
rect1 = Rectangle(5, 3)  # Creating an object of the Rectangle class
print("Area:", rect1.area())  # Calling the area method 
print("Perimeter:", rect1.perimeter())  # Calling the perimeter method



# Static Methods - Methods that belong to the class rather than any object of the class. They do not have access to instance or class attributes.
class MathOperations :
    @staticmethod # decorator to define a static method
    def add(a, b) :  # Static method to add two numbers
        return a + b
    @staticmethod
    def multiply(a, b) :  # Static method to multiply two numbers
        return a * b
    
result1 = MathOperations.add(5, 3)  # Calling the static add method
result2 = MathOperations.multiply(5, 3)  # Calling the static multiply method
print("Addition:", result1)
print("Multiplication:", result2)



# Deleting Objects - Using the del keyword to delete an object.
class Person :
    def __init__(self, name) :
        self.name = name
    def display(self) :
        print("Name:", self.name)

person1 = Person("Charlie")  # Creating an object of the Person class
person1.display()  # Calling the display method
del person1.name  # Deleting the name attribute
# print(person1.name)  # This will raise an error since name is deleted
del person1  # Deleting the object
# person1.display()  # This will raise an error since person1 is deleted



# Four Pillars of OOP ------
# 1. Abstraction - Hiding complex implementation details and showing only the necessary parts.
class Phone :
    def make_call(self, number) :
        print(f"Calling {number}...")
    def send_message(self, number, message) :
        print(f"Sending message to {number}: {message}")

my_phone = Phone()
my_phone.make_call("123-456-7890")  # Abstraction: User doesn't
my_phone.send_message("123-456-7890", "Hello!")  # need to know how these methods work internally


# 2. Encapsulation - Bundling data and methods that operate on that data within a single unit (class).
class BankAccount :
    def __init__(self, balance) :
        self.__balance = balance  # Private attribute
    def deposit(self, amount) :
        self.__balance += amount
    def withdraw(self, amount) :
        if amount <= self.__balance :
            self.__balance -= amount
        else :
            print("Insufficient funds")
    def get_balance(self) :
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())  # Accessing balance via method



# Private Attributes and Methods - Attributes and methods that cannot be accessed directly from outside the class.
class Computer :
    def __init__(self, brand, cpu) :
        self.__brand = brand  # Private attribute
        self.__cpu = cpu      # Private attribute
    def __display_specs(self) :  # Private method
        print(f"Brand: {self.__brand}, CPU: {self.__cpu}")
    def show(self) :
        self.__display_specs()  # Accessing private method within the class
my_computer = Computer("Dell", "Intel i7")
my_computer.show()  # Calling public method to display specs
# my_computer.__display_specs()  # This will raise an error since the method is private



# 3. Inheritance - Mechanism by which a new class can inherit attributes and methods from an existing class.
class Animal :
    def speak(self) :
        print("Animal speaks")
    def info(self) :
        print("This is an animal.")
class Dog(Animal) :  # Dog class inherits from Animal class
    def speak(self) :  # Overriding the speak method
        print("Dog barks")

dog1 = Dog()  # Creating an object of the Dog class
dog1.speak()  # Calling the overridden speak method
dog1.info()   # Calling the inherited info method

# Type of Inheritance:
# 1. Single Inheritance
# 2. Multi-level Inheritance
# 3. Multiple Inheritance


# super() Method - Used to call a method from the parent class.
class Parent :
    def show(self) :
        print("This is the Parent class.")  
class Child(Parent) :
    def show(self) :
        super().show()  # Calling the parent class method
        print("This is the Child class.")

child1 = Child()  # Creating an object of the Child class
child1.show()  # Calling the show method of Child class



# classmethod - A method that is bound to the class and not the instance of the class. It can access class attributes and methods.
class Person1 :
    name = "Unknown"  # Class attribute
    @classmethod
    def set_name(cls, name) :  # Class method to set the name
        cls.name = name
    @classmethod
    def display_name(cls) :  # Class method to display the name
        print("Name:", cls.name)
Person1.set_name("David")  # Calling the class method to set name
Person1.display_name()     # Calling the class method to display name   



# Property Decorators - Used to define getters and setters for class attributes.
class Student2 :
    def __init__(self,phy,chem,math) :
        self._phy = phy
        self._chem = chem
        self._math = math
    # def calcPercentage(self) :
        # self.percentage = (self._phy + self._chem + self._math) / 3
    @property
    def percentage(self) :
        return (self._phy + self._chem + self._math) / 3
    
student3 = Student2(85, 90, 95)  # Creating an object of the Student2 class
print("Percentage:", student3.percentage)  # Accessing percentage using property decorator
# student3.calcPercentage()
# print("Percentage:", student3.percentage)  # Accessing calculated percentage   



# 4. Polymorphism - The ability to present the same interface for different data types.
# Operator Overloading - Defining how operators behave for user-defined classes.
print(1+2)         # Integer addition
print("Hello " + "World")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation

class Vector :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __add__(self, other) :  # Overloading the + operator
        return Vector(self.x + other.x, self.y + other.y)
    def display(self) :
        print(f"Vector({self.x}, {self.y})")

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Using overloaded + operator
v3.display()  # Displaying the result of vector addition

# Method Overloading - Defining multiple methods with the same name but different parameters.
class Calculator :
    def add(self, a, b, c=0) :  # Method with default parameter
        return a + b + c
calc = Calculator()
print("Addition of 2 numbers:", calc.add(5, 10))        # Calling
print("Addition of 3 numbers:", calc.add(5, 10, 15))    # Calling with 3 parameters
# Note: Python does not support traditional method overloading like some other languages. 
# Instead, we can use default parameters or *args to achieve similar functionality.

# dander functions - Special functions that start and end with double underscores (__). They are also known as magic methods.
# Examples include __init__, __str__, __repr__, __add__, etc. They allow
# us to define how objects of a class behave with built-in operations.



# @getter and @setter decorators - Used to define getter and setter methods for class attributes.
class Employee :
    def __init__(self, name, salary) :
        self._name = name
        self._salary = salary
    @property
    def salary(self) :  # Getter for salary
        return self._salary
    @salary.setter
    def salary(self, amount) :  # Setter for salary
        if amount < 0 :
            print("Salary cannot be negative.")
        else :
            self._salary = amount

emp = Employee("Eve", 50000)
print("Salary:", emp.salary)  # Accessing salary using getter
emp.salary = 60000  # Setting salary using setter
print("Updated Salary:", emp.salary)
emp.salary = -1000  # Trying to set a negative salary
# This will print an error message
