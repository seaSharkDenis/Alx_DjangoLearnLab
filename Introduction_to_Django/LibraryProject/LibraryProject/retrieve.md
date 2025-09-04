<!-- Retrieve all obects -->
all_books = Book.objects.all()
for book in all_books:
    print(f"Title: {book.title}, Author: {book.author}")

<!-- Expected Output -->
Title: 1984, Author: George Orwell