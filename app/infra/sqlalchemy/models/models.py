"""Módulo que define as models"""

from sqlalchemy import Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.infra.sqlalchemy.config.database import Base


class Disciplina(Base):
    """Classe que define a disciplina"""

    __tablename__ = 'teste_grade_disciplinas'

    id_disciplina: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
        unique=True,
    )

    codigo: Mapped[str] = mapped_column(
        Text,
    )

    nome: Mapped[str] = mapped_column(
        Text,
    )

    feita: Mapped[bool] = mapped_column(
        Boolean
    )

    horarios: Mapped[str] = mapped_column(
        Text,
    )

    depto: Mapped[str] = mapped_column(
        Text,
    )

    turma: Mapped[str] = mapped_column(
        Text,
    )

    periodo: Mapped[str] = mapped_column(
        Text,
    )

    docente: Mapped[str] = mapped_column(
        Text,
    )

    carga_horaria: Mapped[int] = mapped_column(
        Integer,
    )

    local: Mapped[str] = mapped_column(
        Text,
    )
