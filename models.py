from pydantic import BaseModel
import  datetime
class SignUpSchema(BaseModel):
    username=str
    email:str
    full_name=str
    created_at=datetime.datetime
    password:str
    class Config:
        schema_extra={
            "example":
            {
                "username": "example",

                "email":"example@example.com",
                "full_name": "example",
                "created_at": datetime.datetime.now(),
                "password":"password"
            }
        }
class LoginSchema(BaseModel):
    email:str
    password:str
    class Config:
        schema_extra={
            "example":
            {
                "email":"example@example.com",
                "password":"password"
            }
        }
    