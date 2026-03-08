from models import Book
from utils import validate_price

def create_book():
    price = float(input("Введіть ціну: "))
    title = input("Введіть назву книги: ")
    author = input("Введіть автора: ")
    price = float(input("Введіть ціну: "))
    validate_price(price)
    return Book(title, author, price)

if __name__ == "__main__":
    book = create_book()
    print(f"Книгу '{book.title}' додано!")
