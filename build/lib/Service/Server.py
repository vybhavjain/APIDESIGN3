from concurrent import futures
import logging

import grpc
import Book_pb2 
import Book_pb2_grpc
from Database import data as db

#List of books is stored in a seperate file
list_of_books = db.list_of_books

class BookOperations(Book_pb2_grpc.FunctionalityServicer):

    #Implementation of getBook to retrieve data based on the ISBN value
    def getBook(self, request, context):
        if len(list_of_books) == 0:
            context.set_code(grpc.StatusCode.DATA_LOSS)
            context.set_details('The DB is empty')
            return Book_pb2.Book()

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

        #Here return empty as we already set the context of error message in above two lines
        return Book_pb2.Book()
            
    #Implementation of createBook to create a new temporary book in the DB based on the entered values.
    #These values do not persist once the server has been shut off and restarted
    def createBook(self, request, context):
        if len(list_of_books) != 0:
            for book in list_of_books:
                if book.isbn == request.isbn:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    context.set_details('Book Exists in the database already')
                    #Sending null ISBN as context of error and status code is being sent above
                    return Book_pb2.ISBN()
        list_of_books.append(request)
        return Book_pb2.ISBN(ISBN="this "+ str(request.isbn) + " Added to the DB")


#Function that starts the server and runs it on localhost:50051
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Book_pb2_grpc.add_FunctionalityServicer_to_server(BookOperations(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


#To make sure only a direct run will start the server
if __name__ == '__main__':
    logging.basicConfig()
    serve()


'''
Sample input for createBook
{
  "isbn":"abcd-1234",
  "title":"Title1",
  "author":"author1",
  "rating":5,
  "publishing_year":2012, 
  "genre":"THRILLER"
}

Sample input for getBook
{
  "ISBN":"abcd-1234",
}

'''