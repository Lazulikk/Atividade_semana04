from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.estrutura.database import get_db
from app.core.domain.schemas import UserCreate
from app.core.usos import servico_usuario

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def criar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    return servico_usuario.criar_usuario(db, user)


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return servico_usuario.listar_usuarios(db)


@router.get("/{user_id}")
def buscar_usuario(user_id: int, db: Session = Depends(get_db)):
    return servico_usuario.buscar_usuario(db, user_id)