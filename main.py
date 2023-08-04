import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

# get this from database
posts = [
    {
        'id' : 1, 
        "title" : "This is about Virat Kohli",
        "contents" : "This contains contents about Virat Kohli"
    },
    {
        'id' : 2, 
        "title" : "This is about MS Dhoni",
        "contents" : "This contains contents about MS Dhoni"
    },
    {
        'id' : 3, 
        "title" : "This is about Ravindra Jadeja",
        "contents" : "This contains contents about Ravindra Jadeja"
    }
]

# users list
users = [] # empty intitally

app = FastAPI()

#1 route to test the get request
@app.get("/", tags=["test"])
def greet():
    return {"message" : "Hello World"}

#2 route to get all the posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return { "posts" : posts }

#3 route to particular post by id
@app.get("/posts/{id}", tags=["posts"])
def get_posts_by_id( id : int):
    # selecting for a less value
    if id > len(posts) or id < 1:
        return { "error" : "Invalid ID" }
    else:
        for post in posts:
            if post["id"] == id:
                return { 
                    "post" : post
                 }

#4 Post a blog of post
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_new_post(new : PostSchema):
    new.id = len(posts) + 1
    posts.append(new.dict())
    return { "info" : "Post added"}

#5 User Sign up (create a new user))
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

# Function to check for the existence of the user
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

#6 Login route
@app.post("/user/login", tags=["user"])
def user_login(data: UserLoginSchema = Body(default=None)):
    if check_user(data):
        return signJWT(data.email)
    else:
        return {
            "error" : "Invalid Login Details"
        }

