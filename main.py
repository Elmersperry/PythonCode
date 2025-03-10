from api_library.book import Book
from api_library.library import Library

book_1 = Book(title="Капитанская дочка", author="А. С. Пушкин", year=1836, genre="Роман")

book_2 = Book(title="Герой нашего времени", author="М. Ю. Лермонтов", year=1836, genre="Роман")

library = Library()

library.add_book(book_1)
library.add_book(book_2)

books = library.get_books()
for id_, book in books.items():
    print(book.get_info())