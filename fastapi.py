from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app=FastAPI()
userinfo={}

class User(BaseModel):
    user_name:str
    user_id:int
    user_contact_number:int
 
@app.post("/adduser/")
async def adduser(user:User):
  
    userinfo[user.user_id]={
       "user_name":user.user_name ,"user_contact_number":user.user_contact_number
    }
  
    return JSONResponse(
        status_code=200,
        content={
            "message": "User added successfully",
            "users": userinfo})


@app.get("/user")
async def get_users(user_id:int):
    if user_id in userinfo:
         return JSONResponse(
        status_code=200,
        content={
            "message": "User showed successfully",
            "users": userinfo})

    return JSONResponse(
            status_code=404,
            content={
                "message": "User not in ",
                "users": userinfo
            }
        )
    
   
    

@app.put("/user")
async def updateuser(user_id:int,user:User):
   if user_id in userinfo:
    

    userinfo[user_id] = {
            "user_name": user.user_name,
            "user_contact_number": user.user_contact_number
        }
    return JSONResponse(
            status_code=200,
            content={
                "message": "User updated successfully",
                "users": userinfo
            }
        )
    
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    if user_id in userinfo:
        del userinfo[user_id]
        return JSONResponse(
            status_code=200,
            content={
                "message": "User deleted successfully",
                "users": userinfo
            })
    
    return JSONResponse(
            status_code=404,
            content={
                "message": "User not in ",
                "users": userinfo
            })
       
#@app.get("/{name}")
#def fun(name:str):
    #return {'message:' f"say hello: {name}"}      
