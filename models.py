# models.py
class Book:
    def __init__(self, title, author, price, description=""):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
    def __str__(self):
        return f"{self.title} від {self.author} - {self.price} грн"