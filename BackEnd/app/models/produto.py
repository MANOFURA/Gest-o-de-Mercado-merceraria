from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    descricao = Column(
        String(255),
        nullable=True
    )

    ativo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    categoria = relationship(
        "Categoria",
        back_populates="produtos"
    )