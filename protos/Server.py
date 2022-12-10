from concurrent import futures
import logging

import grpc
import Book_pb2
import Book_pb2_grpc

book1 = Book_pb2.Book(
    isbn = "abcd-1000",
    title = "Divergent",
    author = "Veronica Roth",
    rating = 5,
    publishing_year = 2012,
    genre = "THRILLER"
)

book2 = Book_pb2.Book(
    isbn = "abcd-1001",
    title = "Insurgent",
    author = "Veronica Roth",
    rating = 4,
    publishing_year = 2014,
    genre = "THRILLER"
)


book3 = Book_pb2.Book(
    isbn = "abcd-1002",
    title = "Allegiant",
    author = "Veronica Roth",
    rating = 4,
    publishing_year = 2016,
    genre = "FICTION"
)


list_of_books = [book1,book2,book3]

class BookOperations(Book_pb2_grpc.FunctionalityServicer):

    def getBook(self, request, context):
        global list_of_books

        for book in list_of_books:
            if book.isbn == request.ISBN:
                return Book_pb2.Book(
                    isbn = book.isbn,
                    title = book.title,
                    author = book.author,
                    rating = book.rating,
                    publishing_year = book.publishing_year, 
                    genre = book.genre)

        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Book not found')
        return Book_pb2.Response()
            

    def createBook(self, request, context):
        global list_of_books
        if len(list_of_books) != 0:
            for book in list_of_books:
                if book.isbn == request.isbn:
                    return Book_pb2.ISBN(ISBN="Book with ISBN: " + book.isbn + "already exists in the Database")
        list_of_books.append(request)
        #print("Book created sucessfully")
        return Book_pb2.ISBN(ISBN="this "+ str(request.isbn) + " Added to the DB")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Book_pb2_grpc.add_FunctionalityServicer_to_server(BookOperations(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


'''
{
	"isbn":"abcd-1234",
  "title":"Title1",
  "author":"author1",
  "rating":"5",
  "publishing_year":"2012", 
  "genre":"THRILLER"
}
'''