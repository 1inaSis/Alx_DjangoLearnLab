import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

# Query: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for book in library.books.all():
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

# Query: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian of {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"No librarian found for library {library_name}")

# Sample function calls (replace with real values or use the shell)
# get_books_by_author("Jane Austen")
# get_books_in_library("Central Library")
# get_librarian_for_library("Central Library")
