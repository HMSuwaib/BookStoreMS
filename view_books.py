def view_books(books):
    if not books:
        print("\nNo books available in the store.")
        return

    print("\n--- List of Books ---")
    for idx, book in enumerate(books, start=1):
        print(f"\nBook {idx}:")
        print(f"  Title    : {book['title']}")
        print(f"  Author   : {book['author']}")
        print(f"  ISBN     : {book['isbn']}")
        print(f"  Genre    : {book['genre']}")
        print(f"  Price    : ${book['price']:.2f}")
        print(f"  Quantity : {book['quantity']}")
