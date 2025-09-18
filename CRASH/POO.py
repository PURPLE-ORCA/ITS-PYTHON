# object = a 'bundle' of related attribtes (variables ) abd methods 

# class Car:

# engine_HP = 100 //SHARED VARIABLE CAN BE USED IN ALL THE METHODS

#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print(f'You drive the {self.color} {self.model}')

#     def describe(self):
#         print(f'The {self.color} {self.model} is a {self.year} model')


# car1 = Car('Toyota', 2020, 'red', True)
# car2 = Car('BMW', 2021, 'black', False)

# car1.describe()



# multiple inheritance = inherit from more than one parent class
#                                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                                          C(B) <- B(A) <- A

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")



# Aggregation = Represents a relationship where one object (the whole)
#                           Contains references to one or more INDEPENDENT objects (the parts)

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# library = Library("New York Public Library")

# book1 = Book("Harry Potter...", "J.K. Rowling")
# book2 = Book("The Hobbit", "J. R. R. Tolkein")
# book3 = Book("The Colour of Magic", "Terry Pratchett")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print(library.name)

# for book in library.list_books():
#     print(book)



# Composition = The composed object directly owns its components, which cannot exist independently
#                            "owns-a" relationship

# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self, size):
#         self.size = size

# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

# car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
# car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

# print(car1.display_car())
# print(car2.display_car())



#  Class methods = Allow operations related to the class
#                                Take (cls) as the first parameter, which represents the class itself.

#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself

# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     #INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name} {self.gpa}"

#     @classmethod
#     def get_count(cls):
#         return f"Total # of students: {cls.count}"

#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())




# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                                 They are automatically called by many of Python's built-in operations.
#                                 They allow developers to define or customize the behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#         return self.num_pages > other.num_pages

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author

#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"Key '{key}' was not found"

# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
# book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book1)  # Calls __str__
# print(book1 == book3)  # Calls __eq__
# print(book1 < book2)  # Calls ___lt__
# print(book2 > book3)  # Calls __gt__
# print(book1 + book2)  # Calls __add__
# print("Lion" in book3)  # Calls __contains__
# print(book3['title'])  # Calls __getitem__