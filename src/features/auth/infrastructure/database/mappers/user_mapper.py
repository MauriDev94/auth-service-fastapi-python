from datetime import date, datetime
from src.features.auth.domain.entities.user_entity import User
from src.features.auth.infrastructure.database.models.user_document import UserDocument


def user_entity_to_document(user: User) -> UserDocument:
    """
    Convierte una entidad User del dominio a un documento de MongoDB.

    Args:
        user: Entidad User del dominio

    Returns:
        dict: Documento listo para insertar en MongoDB
    """
    document = {
        "name": user.name,
        "last_name": user.last_name,
        "birth_date": user.birth_date.isoformat(),  # date -> "YYYY-MM-DD"
        "email": user.email,
        "password": user.password,  # Ya debe estar hasheado
    }

    return document


def document_to_user_entity(document: UserDocument) -> User:
    """
    Convierte un documento de MongoDB a una entidad User del dominio.

    Args:
        document: Documento de MongoDB

    Returns:
        User: Entidad User del dominio
    """
    return User(
        id=str(document["_id"]),
        name=document["name"],
        last_name=document["last_name"],
        birth_date=date.fromisoformat(document["birth_date"]),  # "YYYY-MM-DD" -> date
        email=document["email"],
        password=document["password"],
        created_at=document["created_at"],
        updated_at=document["updated_at"],
    )
