from fastapi import APIRouter

router = APIRouter(
    prefix="/inscricoes",
    tags=["Inscricoes"]
)

@router.get("/")
def listar_inscricoes():
    return {"mensagem": "Lista de inscricoes"}