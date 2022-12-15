import inventory_client

#List of hardcoded isbns to test the function
list_of_isbns = ["abcd-1000", "abcd-1001"]

def getBookTitles(list_of_isbns, inventoryclient):
    book_title_list = []
    for isbn in list_of_isbns:
        books = inventoryclient.getBook(isbn)
        book_title_list.append(books.title)
    return book_title_list 


if __name__ == "__main__":
    client = inventory_client.inventoryclient()
    book_title_list = getBookTitles(list_of_isbns,client)
    for title in book_title_list:
        print(title)