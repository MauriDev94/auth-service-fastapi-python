from pydantic import BaseModel
from datetime import date


class RegisterUserRequest(BaseModel):
    name: str
    last_name: str
    birth_date: date
    email: str
    password: str
