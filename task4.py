class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book}" додана.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Книга "{book}" видалена.')
        else:
            print(f'Книга "{book}" не знайдена.')

    def show_books(self):
        if self.books:
            print("Список книг:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
        else:
            print("Книготека порожня.")

library = Library()

library.add_book("Clean Code")
library.add_book("Python")
library.show_books()

library.remove_book("Clean Code")
library.show_books()
