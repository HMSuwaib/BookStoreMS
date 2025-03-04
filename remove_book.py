def remove_book(books):
    isbn_to_remove = input("Enter ISBN/Book ID of the book to remove: ").strip()
    for book in books:
        if book['isbn'] == isbn_to_remove:
            books.remove(book)
            print("Book removed successfully.")
            return
    print("Error: Book with the given ISBN not found.")
