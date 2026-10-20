
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import engine
from src.models.material import VariacaoMaterial


def criar_variacao(
    material_id: int,
    descricao: str,
    codigo_referencia: str | None,
    estoque_minimo: Decimal,
) -> VariacaoMaterial:
    """Cadastra uma variação vinculada a um material."""

    with Session(engine) as sessao:
        variacao = VariacaoMaterial(
            material_id=material_id,
            descricao=descricao,
            codigo_referencia=codigo_referencia,
            estoque_minimo=estoque_minimo,
            ativa=True,
        )

        sessao.add(variacao)
        sessao.commit()
        sessao.refresh(variacao)

        return variacao


def listar_variacoes() -> list[VariacaoMaterial]:
    """Consulta todas as variações cadastradas."""

    with Session(engine) as sessao:
        consulta = select(VariacaoMaterial).order_by(
            VariacaoMaterial.material_id,
            VariacaoMaterial.descricao,
        )

        return list(sessao.scalars(consulta).all())
