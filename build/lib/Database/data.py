#File containing the List with pre recorded data about different available books in the Library
#We store the existing books in this file and import this value in the server file to add new books/check existing books in the
#Library system

from Service import Book_pb2

#Creating a sample book to add to the library system
book1 = Book_pb2.Book(
    isbn = "abcd-1000",
    title = "Divergent",
    author = "Veronica Roth",
    rating = 5,
    publishing_year = 2012,
    genre = "THRILLER"
)

#Creating a sample book to add to the library system
book2 = Book_pb2.Book(
    isbn = "abcd-1001",
    title = "Insurgent",
    author = "Veronica Roth",
    rating = 4,
    publishing_year = 2014,
    genre = "THRILLER"
)

#Creating a sample book to add to the library system
book3 = Book_pb2.Book(
    isbn = "abcd-1002",
    title = "Allegiant",
    author = "Veronica Roth",
    rating = 4,
    publishing_year = 2016,
    genre = "FICTION"
)

list_of_books = [book1,book2,book3]