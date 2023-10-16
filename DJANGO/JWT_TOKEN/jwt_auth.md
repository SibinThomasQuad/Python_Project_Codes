Certainly, here's a simple example of a Django REST framework project with custom authentication views for user login, token retrieval, and a set of views to manage books. You can customize this example further to suit your needs:

1. **Create a Django Project and App**:

   Start by creating a Django project and a new app:

   ```bash
   django-admin startproject jwt_example
   cd jwt_example
   python manage.py startapp books
   ```

2. **Install Required Packages**:

   Install the necessary packages:

   ```bash
   pip install djangorestframework djangorestframework-jwt
   ```

3. **Update Settings**:

   Update your project's `settings.py` as follows:

   ```python
   # settings.py

   INSTALLED_APPS = [
       # ...
       'rest_framework',
       'rest_framework_jwt',
       'books',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
       ),
   }

   JWT_AUTH = {
       'JWT_ALLOW_REFRESH': True,
       'JWT_EXPIRATION_DELTA': timedelta(hours=1),
       'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
   }
   ```

4. **Create Authentication Views**:

   In your app's `views.py`, define custom authentication views for user login and token retrieval:

   ```python
   # books/views.py
   from django.contrib.auth import authenticate, login
   from rest_framework import status
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   from rest_framework_jwt.settings import api_settings

   @api_view(['POST'])
   def user_login(request):
       username = request.data.get('username')
       password = request.data.get('password')

       user = authenticate(request, username=username, password=password)

       if user:
           login(request, user)
           jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
           jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
           payload = jwt_payload_handler(user)
           token = jwt_encode_handler(payload)
           return Response({'token': token}, status=status.HTTP_200_OK)
       else:
           return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
   ```

5. **Create Book Views**:

   Create views for managing books (e.g., list, create, delete) in `books/views.py`:

   ```python
   # books/views.py
   from rest_framework.decorators import api_view, permission_classes
   from rest_framework.permissions import IsAuthenticated
   from rest_framework.response import Response
   from rest_framework import status
   from .models import Book
   from .serializers import BookSerializer

   @api_view(['GET'])
   @permission_classes([IsAuthenticated])
   def book_list(request):
       books = Book.objects.all()
       serializer = BookSerializer(books, many=True)
       return Response(serializer.data)

   @api_view(['POST'])
   @permission_classes([IsAuthenticated])
   def create_book(request):
       serializer = BookSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   @api_view(['DELETE'])
   @permission_classes([IsAuthenticated])
   def delete_book(request, book_id):
       try:
           book = Book.objects.get(id=book_id)
       except Book.DoesNotExist:
           return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
       
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   ```

6. **Define Book Model and Serializer**:

   Create a model for books and a serializer in `books/models.py` and `books/serializers.py`:

   ```python
   # books/models.py
   from django.db import models

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.CharField(max_length=100)

   # books/serializers.py
   from rest_framework import serializers
   from .models import Book

   class BookSerializer(serializers.ModelSerializer):
       class Meta:
           model = Book
           fields = '__all__'
   ```

7. **Define URLs**:

   Define the URLs for your custom authentication views and book views in `books/urls.py`:

   ```python
   # books/urls.py
   from django.urls import path
   from .views import user_login, book_list, create_book, delete_book

   urlpatterns = [
       path('login/', user_login, name='user_login'),
       path('books/', book_list, name='book_list'),
       path('books/create/', create_book, name='create_book'),
       path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
   ]
   ```

8. **Configure Main URLs**:

   In your project's `urls.py`, include the app's URLs:

   ```python
   # jwt_example/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('books.urls')),
   ]
   ```

9. **Create the Database and Apply Migrations**:

   Run the following commands to create the database and apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

10. **Run the Development Server**:

    Start the development server:

    ```bash
    python manage.py runserver
    ```

Now you have a Django REST framework project with custom authentication views for user login and token retrieval and views for managing books. You can use Postman or any API client to test the authentication and book management endpoints. To obtain a token, send a POST request to `/api/login/` with valid user credentials
