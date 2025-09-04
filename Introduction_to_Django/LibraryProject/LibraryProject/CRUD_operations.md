<!-- Create book instance -->
book_instance = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- Expected Output -->
<Book: Book object (1)>

<!-- Retrieve Book instance -->
all_books = Book.objects.all()
for book in all_books:
    print(f"Title: {Book.title}, Author: {Book.author}")

<!-- Expected Output -->
Title: 1984, Author: George Orswell

<!-- Update a Book Instance -->
book_update = Book.objects.get(title="1984")
book_update.title = "Nineteen Eighty-Four"
book_update.save()


<!-- Delete a book instance -->
delete_book = Book.objects.get(title="Nineteen Eighty-Four")
delete_book.delete()

<!-- Expected output -->
(1, {'bookshelf.Book': 1})