#LIBRARY MANAGEMENT SYSTEM
'''###   lms===== library management system
#         project idea
# ================================


# library-- main idea

# books- what type of books,how many books,
# members- noof members
# library--- add a book, remote book, registration,issue book,
# return book,search book,
# display deatils'''

### basic book class



### abstraction
from abc import ABC,abstractmethod
import re

class LibraryItem(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def get_type(self):
        pass

class Book(LibraryItem):
    total_book=0
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.__is_avialable=True
        Book.total_book+=1

### encapulation--- it is used in this  program we don"t want anyone
#  modify important information

    def issue_book(self):
        if self.__is_avialable:
            self.__is_avialable=False
            print("Book isuued successfully")
        else:
            print('book is already issued')

    def return_book(self):
        self.__is_avialable=True
        print('Book returned successfully')

    def is_avialable(self):
        return self.__is_avialable

    def display(self):
        print('book_id:',self.book_id)
        print('Title:',self.title)
        print('Author:',self.author)
        print('Available:',self.is_avialable())
    def get_type(self):
        return "Book"

    ### operator overloading
    def __eq__(self,other):
        if isinstance(other,Book):
            return self.book_id==other.book_id
        return  False
    def __str__(self):
        return f"{self.title}by {self.author}"

## class of ebook
class Ebook(Book):
    def __init__(self, book_id, title, author,filesize):
        super().__init__(book_id, title, author)
        self.filesize=filesize
    ## method overriding
    def issue_book(self):
        print(f"{self.title}'E book access granted ")

    def  get_type(self):
        return 'E book'
    def display(self):
        print(
            f"ID:{self.book_id}|"
            f"Title:{self.title}|"
            f"Author:{self.author}|"
            f"Filesize:{self.filesize}"
        )

## printed book
class PrintedBook(Book):
    def __init__(self, book_id, title, author,pages):
        super().__init__(book_id, title, author)
        self.pages=pages

    def issue_book(self):
        if self.is_avialable():
            print(f"printed book '{self.title}'issued physically.")
            super().issue_book()
        else:
            print("book already issued.")
    def get_type(self):
        return "printed book"
    def display(self):
        super().display()
        print("pages:",self.pages)

## member  class

class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
    def borrow_book(self,book):
        if book.is_avialable:
            book.issue_book()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title}is not available.")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name}returned {book.title}")
        else:
            print("book was not boorowed by this member.")

    def display_member(self):
        print('\n member ID:',self.member_id)
        print("name:",self.name)
        print('Borrowed books:')
        if not self.borrowed_books:
            print("No books Borrowed.")
        else:
            for book in self.borrowed_books:
                print("-",book)

### student member
class student_member(Member):
    def __init__(self, member_id, name,college):
        super().__init__(member_id, name)
        self.college=college
    
    def display_member(self):
        super().display_member()
        print('college:',self.college)

## faculty member
class faculty_member(Member):
    def __init__(self, member_id, name,department):
        super().__init__(member_id, name)
        self.department=department
    
    def display_member(self):
        super().display_member()
        print('Department:',self.department)

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]

    ## add a book
    def add_book(self,book):
        self.books.append(book)
        print(f'Book  {book.title} added successfully.')        

    def remove_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                self.books.remove(book)
                print("Books removed successfully.")
                return 
        print("Book not found")

    ##register member
    def register_member(self,member):
        self.members.append(member)
        print(f'member {member.name} added successfully.')

    # search book
    def search_book(self,title=None,author=None):
        found=False
        for book in self.books:
            if(title and title.lower() in book.title.lower()):
                book.display()
                found=True
            elif (author and author.lower() in book.author.lower()):
                book.display()
                found=True
        if not found:
            print('no book found.')

    ## display books
    def display_books(self):
        print("\n ----------Library books------:")
        if not self.books:
            print('No books available')
            return
        for book in self.books:
            book.display()

    ## display members
    def display_members(self):
        print("\n-----Members-------")
        for member  in  self.members():
            member.display_member()

    # find member
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id==member_id:
                return member
        return None

    # find book
     
    def find_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                return book
        return None

library=Library('ABC central library')
book1=Book(101,'python','Guido')
book2=PrintedBook(102,'java','van',500)
book3=Ebook(103,'ml','Andrew','10mb')
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
student=student_member(1,'Vivek','GVP college')
faculty=faculty_member(2,"Dr.Murthy",'CSE')
library.register_member(student)
library.register_member(faculty)
library.display_books()
student.borrow_book(book1)
student.display_member()
student.return_book(book1)
library.search_book(title='python')
library.search_book(author='van')


    


        
      
       