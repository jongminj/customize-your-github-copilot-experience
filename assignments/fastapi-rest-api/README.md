# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for a small book catalog using FastAPI. You will practice defining routes, validating request data with Pydantic, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the API and List Books

#### Description
Use the attached starter code to create a FastAPI application for managing books. Install FastAPI and Uvicorn with `pip install fastapi uvicorn`, then start the server with `uvicorn main:app --reload`.

#### Requirements
Completed program should:

- Return `{"status": "ok"}` from `GET /health`
- Return all books as a JSON array from `GET /books`
- Use the provided in-memory book collection; a database is not required
- Open the interactive API documentation at `/docs`


### 🛠️ Add and Find Books

#### Description
Add endpoints for retrieving one book and creating a book. Use the provided Pydantic model to validate incoming book data.

#### Requirements
Completed program should:

- Return the matching book from `GET /books/{book_id}`
- Return HTTP `404 Not Found` when the requested book ID does not exist
- Create a book from a JSON request to `POST /books` and assign it a unique integer ID
- Return the created book with HTTP `201 Created`
- Reject a blank title, blank author, or year earlier than 1450 with a validation error

Example request body:

```json
{
  "title": "The Time Machine",
  "author": "H. G. Wells",
  "year": 1895
}
```


### 🛠️ Update and Delete Books

#### Description
Complete the book catalog's CRUD operations by adding endpoints to replace an existing book and delete it.

#### Requirements
Completed program should:

- Replace a book's title, author, and year with `PUT /books/{book_id}`
- Return the updated book, or HTTP `404 Not Found` if the ID does not exist
- Delete a book with `DELETE /books/{book_id}`
- Return HTTP `204 No Content` after a successful deletion, or HTTP `404 Not Found` if the ID does not exist
- Verify the endpoints and error responses using `/docs` or an HTTP client
