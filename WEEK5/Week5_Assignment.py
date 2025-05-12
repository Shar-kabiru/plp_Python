# # Assignment 1: Design Your Own Class! 
# # Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# # Add attributes and methods to bring the class to life!

class Book:
    #Attributes
    Library = "Kenya National Library"

    def lib(self):
        print("The library is great")

my_book = Book()
print(my_book.Library)
my_book.lib()

# # Use constructors to initialize each object with unique values.
# # Constructors
class Book:
    def __init__(self):
        self.title = input("Enter the Title of the book: ")
        self.author = input("Who is the author: ")
    #Methods
    def book_Author(self):
        print(f'The author of "{self.title}" is "{self.author}"')
my_book = Book()
my_book.book_Author()

# # Add an inheritance lajyer to explore polymorphism or encapsulation.

# #Inheritance
class journal(Book):
    pass

journal = Book()
print (journal.title)

# # Poly morphism
class Movie:
    def title(self):
        self.movieName = input("Enter the Title of the Movie: ")
        return self.movieName
    
class Show:
    def title(self):
        self.showName = input("Enter the Title of the Show: ")
        return self.showName
    
for videos in [Movie(), Show()]:
    print(videos.title())

#Encapsulation
class Series:
    def __init__(self):
        self.__episodes = 3 # Private attribute

    def seen_episodes(self):
        if self.__episodes > 0:
            self.__episodes -= 1
            print("You've seen this episode")
        else:
            print("You've seen all episodes")
stash = Series()
stash.seen_episodes()
stash.seen_episodes()
stash.seen_episodes()
stash.seen_episodes()
# Activity 2: Polymorphism Challenge! 

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" , while Plane.move() prints "Flying" ).

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"
    
for transport in [Car(), Plane()]:
    print(transport.move())