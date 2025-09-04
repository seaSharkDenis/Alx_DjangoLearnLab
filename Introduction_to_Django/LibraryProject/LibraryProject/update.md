<!-- Update the 1984 record -->
book_update = Book.objects.get(title="1984")
book_update.title ="Nineteen Eighty-Four"
book_update.save()