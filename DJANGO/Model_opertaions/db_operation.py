# Import Django modules
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.db import connection
from django.conf import settings
from django.core.management import execute_from_command_line

# Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ],
    ROOT_URLCONF=__name__,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }
)

# Define a Django model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

# Django views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    new_book = Book(title='A New Book', author='John Doe', publication_date='2023-01-01')
    new_book.save()
    return HttpResponse("Book added successfully")

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.title = 'Updated Title'
    book.save()
    return HttpResponse("Book updated successfully")

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponse("Book deleted successfully")

def books_published_after(request, year):
    books = Book.objects.filter(publication_date__year__gt=year)
    return render(request, 'book_list.html', {'books': books})

def filter_by_id(request, book_id):
    books = Book.objects.filter(id=book_id)
    return render(request, 'book_list.html', {'books': books})

def raw_query(request):
    raw_sql_query = """
    SELECT * FROM myapp_book
    WHERE publication_date >= '2023-01-01';
    """
    
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query)
        raw_query_result = cursor.fetchall()
    
    return render(request, 'book_list.html', {'books': raw_query_result})

# URL routing
urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('update_book/<int:book_id>/', update_book, name='update_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('books_published_after/<int:year>/', books_published_after, name='books_published_after'),
    path('filter_by_id/<int:book_id>/', filter_by_id, name='filter_by_id'),
    path('raw_query/', raw_query, name='raw_query'),
]

# URL configuration
if __name__ == "__main__":
    execute_from_command_line()
