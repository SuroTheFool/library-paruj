class Book:
    def __init__(self,id,title,author,total_copies,available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

# class Member:
#     def __init__(self,id,name, email, borrowed_books,list):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.borrowed_books = borrowed_books
#         self.list = list

class Library():
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")


# MAIN
library = Library()
b = Book(1,"The Father Goriot","Honoré de Balzac",100,20)
b1 = Book(2,"The Miserables","Victor Hugo", 300, 20 )

library.add_book(b)
library.add_book(b1)