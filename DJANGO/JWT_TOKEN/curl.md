To test the API with `curl`, you can use the following commands for different operations, including user login, creating a book, listing books, and deleting a book. Remember to replace the placeholders (e.g., `<username>`, `<password>`, `<token>`, `<book_id>`) with actual values.

1. **User Login and Token Retrieval**:

   To authenticate a user and obtain a JWT token:

   ```bash
   curl -X POST http://localhost:8000/api/login/ -d "username=<username>&password=<password>"
   ```

   Replace `<username>` and `<password>` with valid user credentials. This command will return a JSON response containing a token.

2. **List Books (Authenticated)**:

   To list books, you need to include the JWT token obtained from the previous step:

   ```bash
   curl -X GET http://localhost:8000/api/books/ -H "Authorization: JWT <token>"
   ```

   Replace `<token>` with the JWT token you received after login.

3. **Create a Book (Authenticated)**:

   To create a new book, provide the book data and the JWT token:

   ```bash
   curl -X POST http://localhost:8000/api/books/create/ -d "title=New Book Title&author=Book Author" -H "Authorization: JWT <token>"
   ```

   Replace `<token>` with the JWT token.

4. **Delete a Book (Authenticated)**:

   To delete a book, specify the book ID and the JWT token:

   ```bash
   curl -X DELETE http://localhost:8000/api/books/delete/<book_id>/ -H "Authorization: JWT <token>"
   ```

   Replace `<book_id>` with the ID of the book to delete and `<token>` with the JWT token.

Make sure your Django development server is running on `http://localhost:8000` or adjust the URLs accordingly.
