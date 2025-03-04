def add_book(books):
    print("\n--- Add a New Book ---")
    print("Type 'cancel' to cancel adding the book.")


    while True:
        title = input("Enter the book title: ").strip()
        if title.lower() == 'cancel':
            print("Book addition canceled.")
            return
        if title:
            break
        print("Error: Book title cannot be empty. Please try again.")


    while True:
        author = input("Enter the author name: ").strip()
        if author.lower() == 'cancel':
            print("Book addition canceled.")
            return
        if author:
            break
        print("Error: Author name cannot be empty. Please try again.")


    while True:
        isbn = input("Enter ISBN/Book ID: ").strip()
        if isbn.lower() == 'cancel':
            print("Book addition canceled.")
            return
        if not isbn:
            print("Error: ISBN/Book ID cannot be empty. Please try again.")
            continue
        if any(book['isbn'] == isbn for book in books):
            print("Error: A book with this ISBN already exists. Please try a different ISBN.")
            continue
        break


    while True:
        genre = input("Enter the genre: ").strip()
        if genre.lower() == 'cancel':
            print("Book addition canceled.")
            return
        if genre:
            break
        print("Error: Genre cannot be empty. Please try again.")


    while True:
        user_input = input("Enter the price: ").strip()
        if user_input.lower() == 'cancel':
            print("Book addition canceled.")
            return
        try:
            price = float(user_input)
            if price <= 0:
                print("Error: Price must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value for the price.")


    while True:
        user_input = input("Enter quantity in stock: ").strip()
        if user_input.lower() == 'cancel':
            print("Book addition canceled.")
            return
        try:
            quantity = int(user_input)
            if quantity < 0:
                print("Error: Quantity must be a non-negative integer. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter an integer for the quantity.")


    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }

    books.append(book)
    print("Book added successfully!")
