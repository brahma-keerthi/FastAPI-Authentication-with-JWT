from pydantic import BaseModel, Field, EmailStr

# Format of the POST method
class PostSchema( BaseModel ):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)

    class config():
        schema_extra = {
            "post_extra" : {
                "title" : "some title about computers",
                "content" : "some content about computers"
            }
        }

class UserSchema( BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)

    class Config:
        the_extra = {
            "user_demo" : {
                "name" : "Sirji",
                "email" : "sirji@gmail.com",
                "password" : "qwe123"
            }
        }

class UserLoginSchema( BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)

    class Config:
        the_extra = {
            "user_demo" : {
                "email" : "sirji@gmail.com",
                "password" : "qwe123"
            }
        }