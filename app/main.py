from fastapi import FastAPI

from app.api.v1.rotas_usuario import router as user_router
from app.api.v1.rotas_curso import router as curso_router
from app.api.v1.rotas_inscricoes import router as inscricao_router

from app.core.estrutura.database import Base, engine
from app.core.estrutura import modelos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudyManager API")

app.include_router(user_router)
app.include_router(curso_router)
app.include_router(inscricao_router)