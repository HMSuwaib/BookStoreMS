def search_book(books):
    search_term = input("Enter title or ISBN to search: ").strip().lower()
    found = False
    for book in books:
        if search_term in book['title'].lower() or search_term == book['isbn'].lower():
            print("\nBook found:")
            print(f"  Title    : {book['title']}")
            print(f"  Author   : {book['author']}")
            print(f"  ISBN     : {book['isbn']}")
            print(f"  Genre    : {book['genre']}")
            print(f"  Price    : ${book['price']:.2f}")
            print(f"  Quantity : {book['quantity']}")
            found = True
    if not found:
        print("No matching book found.")
