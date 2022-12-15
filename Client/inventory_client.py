import grpc
import os 
import sys
sys.path.append(os.path.dirname(__file__) + '/../Service')

from Service import Book_pb2
from Service import Book_pb2_grpc

class inventoryclient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = Book_pb2_grpc.FunctionalityStub(self.channel)

    def getBook(self, ISBN):
        return self.stub.getBook(Book_pb2.ISBN(ISBN=ISBN))

    def createBook(self, isbn, title, author, rating, publishing_year, genre):
        return self.stub.createBook(
            Book_pb2.Book(isbn=isbn, title=title, author=author, rating=rating, publishing_year= publishing_year, genre=genre))