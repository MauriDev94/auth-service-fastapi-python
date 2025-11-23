from dataclasses import dataclass
from datetime import date


@dataclass
class RegisterUserParams:
    name: str
    last_name: str
    birth_date: date
    email: str
    password: str
