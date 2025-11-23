from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class User:
    id: str
    name: str
    last_name: str
    birth_date: date
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
