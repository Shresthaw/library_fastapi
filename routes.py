from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import get_db
import services

router = APIRouter()

#author
@router.post("/authors")
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return services.create_author(db, author)

@router.get("/authors")
def get_authors(db: Session = Depends(get_db)):
    return services.get_authors(db)

@router.get("/authors/{author_id}")
def get_author(author_id:int, db: Session= Depends(get_db)):
    author= services.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author


#bOOK
@router.post("/books")
def create_book(book: schemas.BookCreate, db:Session= Depends(get_db)):
    return services.create_book(db, book)

@router.get("/books")
def get_books(skip:int =0, limit:int = 10, db:Session = Depends(get_db)):
    return services.get_books(db, skip, limit)

@router.get("/books/{book_id}")
def get_book(book_id: int, db:Session = Depends(get_db)):
    return services.get_book(db, book_id)

#adding update
@router.put("/books/{book_id}")
def update_book(book_id:int, book: schemas.BookCreate, db: Session= Depends(get_db)):
    updated= services.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated

#deleting book
@router.delete("/books/{book_id}")
def delete_book(book_id: int, db:Session = Depends(get_db)):
    deleted= services.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"messages": "Deleted sucessfully"}

    
#filtering by author
@router.get("/books/by-author/{author_id}")
def get_books_by_authors(author_id:int, db:Session= Depends(get_db)):
    return services.get_books_by_authors(db, author_id)


#add search
@router.get("/books/search")
def search_book(q:str, db:Session= Depends(get_db)):
    return services.search_book(db, q)

#join query
@router.get("/books-join")
def get_book_join(db:Session = Depends(get_db)):
    return services.get_book_join(db)
