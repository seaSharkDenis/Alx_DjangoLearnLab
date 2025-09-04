<!-- Comman to create a book instance -->
<!-- Shell Initialization -->
python manage.py shell

<!-- Imporing model -->
from bookshelf.models import book

<!-- Creating a new instance -->
book_instance = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- Expected Output -->
The object instance
<Book: Book object (1)>