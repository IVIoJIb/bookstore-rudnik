from models import Book


def create_book():
    title = input("Введіть назву книги: ")
    author = input("Введіть автора: ")
    price = float(input("Введіть ціну: "))

    # Замість log_action додаємо простий print іншою мовою
    print(f"[DEBUG]: Action performed - Created book object: '{title}'")

    return Book(title, author, price)


if __name__ == "__main__":
    book = create_book()
    print(f"Книгу '{book.title}' додано!")