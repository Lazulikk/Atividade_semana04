from sqlalchemy.orm import Session
from .modelos import User, Course, Enrollment


def criar_usuario(db: Session, user):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def listar_usuarios(db: Session):
    return db.query(User).all()


def buscar_usuario(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()