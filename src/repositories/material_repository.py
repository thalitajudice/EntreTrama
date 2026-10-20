
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import engine
from src.models.material import Material


def criar_material(
    nome: str,
    categoria: str,
    unidade_controle: str,
    marca: str | None = None,
) -> Material:
    """Cadastra um novo material no banco de dados."""

    with Session(engine) as sessao:
        material = Material(
            nome=nome,
            marca=marca,
            categoria=categoria,
            unidade_controle=unidade_controle,
            ativo=True,
        )

        sessao.add(material)
        sessao.commit()
        sessao.refresh(material)

        return material


def listar_materiais() -> list[Material]:
    """Consulta os materiais cadastrados."""

    with Session(engine) as sessao:
        consulta = select(Material).order_by(Material.nome)
        materiais = sessao.scalars(consulta).all()

        return list(materiais)