"""Módulo que define o repositório de disciplinas"""

from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas import schemas
from app.infra.sqlalchemy.models import models


class RepoDisciplina():
    """Classe que define as funções referentes às Disciplinas"""

    def __init__(self, session: Session):
        self.session = session

    def criar(
        self,
        id_disciplina: str,
        codigo: str,
        nome: str,
        feita: bool,
        horarios: str,
        depto: str,
        turma: str,
        periodo: str,
        docente: str,
        carga_horaria: str,
        local: str,
    ) -> models.Disciplina:
        """Retorna uma disciplina no banco"""

        db_disciplina = models.Disciplina(
            id_disciplina=id_disciplina,
            codigo=codigo,
            nome=nome,
            feita=feita,
            horarios=horarios,
            depto=depto,
            turma=turma,
            periodo=periodo,
            docente=docente,
            carga_horaria=carga_horaria,
            local=local,
        )

        return db_disciplina

    def listar(self) -> List[schemas.Disciplina]:
        """Retorna todas as disciplinas do banco"""

        stmt = select(models.Disciplina)
        disciplinas = self.session.execute(stmt).scalars().all()

        return disciplinas
