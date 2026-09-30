from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=100, strip_whitespace=True)
    author: str = Field(min_length=1, max_length=100, strip_whitespace=True)
    year: int = Field(ge=1450)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="Frankenstein", author="Mary Shelley", year=1818),
    2: Book(id=2, title="The Hobbit", author="J. R. R. Tolkien", year=1937),
}
next_book_id = 3


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the requested book or raise HTTP 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Assign a unique ID, save the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookInput):
    # TODO: Replace the requested book or raise HTTP 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the requested book or raise HTTP 404.
    pass
