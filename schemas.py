from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author_id: int

class AuthorCreate(BaseModel):
    name: str

class BookResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

class AuthorResponse(BaseModel):
    id: int
    name: str
    books: list[BookResponse]= []

    class Config:
        from_attributes = True