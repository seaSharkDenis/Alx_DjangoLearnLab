<!-- Imporing model -->
from bookshelf.models import Book

delete_book = Book.objects.get(title="Nineteen Eighty-Four")
delete_book.delete()

<!-- Expected Output -->
(1, {'bookshelf.Book': 1})