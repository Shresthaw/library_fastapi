from sqlalchemy.orm import Session
import models

#Author
def create_author(db: Session, author):
    db_author = models.Author(name= author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db:Session):
    return db.query(models.Author).all()

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

#Book
def create_book(db:Session, book):
    db_book = models.Book(title= book.title, author_id= book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip=0, limit=10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db:Session, book_id: int, book):
    db_book = get_book(db,book_id)
    if not db_book:
        return None
    db_book.title = book.title
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db:Session, book_id: int):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return True

def get_books_by_authors(db:Session, author_id:int):
    return db.query(models.Book).filter(models.Book.author_id == author_id).all()

def search_book(db:Session, q:str):
    return db.query(models.Book).filter(models.Book.title.ilike(f"%{q}%")).all()

#join
def get_book_join(db:Session):
    #results= db.query(models.Author, models.Book).join(models.Author).all()
    results = db.query(models.Book, models.Author).join(models.Author, models.Book.author_id == models.Author.id).all()

    data = []
    for book, author in results:
        data.append({
            "book_id": book.id,
            "title": book.title,
            "author_name": author.name
        })
    return data