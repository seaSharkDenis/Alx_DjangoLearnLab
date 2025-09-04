<!-- Retrieve all obects -->
<!-- all_books = Book.objects.all() -->
<!-- for book in all_books:
    print(f"Title: {book.title}, Author: {book.author}") -->

<!-- Retrieval of a single model instance -->
book_instance = Book.objects.get(id=1)

<!-- Expected Output -->
Title: 1984, Author: George Orwell