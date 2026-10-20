from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Material(Base):
    __tablename__ = "materiais"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    marca: Mapped[str | None] = mapped_column(String(100),nullable=True,)
    categoria: Mapped[str] = mapped_column(String(100), nullable=False)
    unidade_controle: Mapped[str] = mapped_column(String(20), nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    variacoes: Mapped[list["VariacaoMaterial"]] = relationship(
        back_populates="material"
    )


class VariacaoMaterial(Base):
    __tablename__ = "variacoes_materiais"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    material_id: Mapped[int] = mapped_column(
        ForeignKey("materiais.id"),
        nullable=False,
    )
    descricao: Mapped[str] = mapped_column(String(150), nullable=False)
    codigo_referencia: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )
    estoque_minimo: Mapped[Decimal] = mapped_column(
        Numeric(12, 3),
        default=0,
        nullable=False,
    )
    ativa: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    material: Mapped["Material"] = relationship(
        back_populates="variacoes"
    )
