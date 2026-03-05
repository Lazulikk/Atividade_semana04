from fastapi import APIRouter

router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"]
)

@router.get("/")
def listar_cursos():
    return {"mensagem": "Lista de cursos"}