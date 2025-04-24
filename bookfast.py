from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app=FastAPI()
books={}

class Book(BaseModel):
    book_name:str
    book_id:int
    aut_name:str

@app.post("/book")
async def addbook(book:Book):
    books[book.book_id]={'book_name':book.book_name,'aut_name':book.aut_name}
    return JSONResponse(
        status_code=200,
          content={"message":'book added successfullly',
                   "book":books})
@app.get("/book")
async def getbook(book_id:int):
    if book_id in books:
        return JSONResponse(
            status_code=200,
            content={"message":"book found successsfully",
                     "books":books})
    else:
        return JSONResponse(
            status_code=404,
            content={'message':"book not found",
                     "In this library":books}
        )
@app.put("/book")
async def updbook(book_id:int,book:Book) :
    if book_id in books:
        books[book.book_id]={'book_name':book.book_name,'aut_name':book.aut_name} 
        return JSONResponse(
            status_code=200,
            content={'message':'book updated sucessfully',
                     'book':books}
        )  
    
@app.delete("/book")
async def deletebook(book_id:int):    
    if book_id in books:
        del books[book_id]
        return JSONResponse(
            status_code=200,
            content={'message':'book deleted successfully',
                     'book':books}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={'message':"book not found",
                     "in this library":books}
        )