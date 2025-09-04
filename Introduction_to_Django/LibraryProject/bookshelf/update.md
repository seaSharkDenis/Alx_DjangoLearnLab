<!-- Update the 1984 record -->
book = Book.objects.get(title="1984")
book.title ="Nineteen Eighty-Four"
book.save()