To update the code with Basic Authentication for your Django REST framework API, you can make use of the `rest_framework.authentication.BasicAuthentication` class provided by Django REST framework. Here's how you can modify your code to include Basic Authentication:

1. In your Django project's settings (typically in `settings.py`), add `BasicAuthentication` to the `DEFAULT_AUTHENTICATION_CLASSES` setting in the REST framework configuration:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    # ... other settings ...
}
```

2. Now, you can use `curl` with the `-u` option to provide Basic Authentication credentials in the form of `username:password` while making requests. Here are the `curl` examples updated with Basic Authentication:

   - **View All Books (GET Request):**

     ```bash
     curl -u your_username:your_password http://localhost:8000/api/books/
     ```

   - **Insert a New Book (POST Request):**

     ```bash
     curl -u your_username:your_password -X POST http://localhost:8000/api/books/ -H "Content-Type: application/json" -d '{
         "title": "Sample Book",
         "author": "John Doe",
         "published_date": "2023-10-14"
     }'
     ```

   - **Retrieve a Book by Primary Key (GET Request):**

     Replace `{book_id}` with the actual primary key of the book you want to retrieve.

     ```bash
     curl -u your_username:your_password http://localhost:8000/api/books/{book_id}/
     ```

   - **Update a Book by Primary Key (PUT Request):**

     Replace `{book_id}` with the actual primary key of the book you want to update.

     ```bash
     curl -u your_username:your_password -X PUT http://localhost:8000/api/books/{book_id}/ -H "Content-Type: application/json" -d '{
         "title": "Updated Book Title",
         "author": "Updated Author Name",
         "published_date": "2023-10-15"
     }'
     ```

   - **Delete a Book by Primary Key (DELETE Request):**

     Replace `{book_id}` with the actual primary key of the book you want to delete.

     ```bash
     curl -u your_username:your_password -X DELETE http://localhost:8000/api/books/{book_id}/
     ```

Replace `your_username` and `your_password` with your actual authentication credentials. This will provide Basic Authentication with your `curl` requests, and your Django REST framework API will require valid username and password credentials for these requests.
