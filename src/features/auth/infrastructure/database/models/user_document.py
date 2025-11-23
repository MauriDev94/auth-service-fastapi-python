from datetime import datetime, date
from typing import TypedDict, Optional
from bson import ObjectId


class UserDocument(TypedDict):
    """
    Estructura del documento de usuario en MongoDB.
    Representa cómo se guarda el usuario en la base de datos.
    """

    _id: Optional[ObjectId]  # MongoDB lo crea automáticamente si no se provee
    name: str
    last_name: str
    birth_date: str  # Formato ISO: "YYYY-MM-DD"
    email: str
    password: str  # Hashed password
    created_at: datetime
    updated_at: datetime


# Ejemplo de documento para referencia:
EXAMPLE_USER_DOCUMENT = {
    "_id": ObjectId("507f1f77bcf86cd799439011"),
    "name": "Mauricio",
    "last_name": "Salinas",
    "birth_date": "1995-05-15",
    "email": "mauri@example.com",
    "password": "$2b$12$KIXxGVGJZ5b7YnXZqE5aHO...",
    "created_at": datetime(2024, 11, 20, 10, 30, 0),
    "updated_at": datetime(2024, 11, 20, 10, 30, 0),
}
