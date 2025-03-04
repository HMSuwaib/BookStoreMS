import json
import os

FILE_NAME = 'books.json'

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                books = json.load(file)
                return books
            except json.JSONDecodeError:
                print("Error: File is corrupted. Starting with an empty list.")
                return []
    else:
        print("No existing data found. Starting fresh.")
        return []

def save_books(books):
    with open(FILE_NAME, 'w') as file:
        json.dump(books, file, indent=4)
