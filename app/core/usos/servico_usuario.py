from sqlalchemy.orm import Session
from app.core.estrutura import repositorios


def criar_usuario(db: Session, user):
    return repositorios.criar_usuario(db, user)


def listar_usuarios(db: Session):
    return repositorios.listar_usuarios(db)


def buscar_usuario(db: Session, user_id: int):
    return repositorios.buscar_usuario(db, user_id)