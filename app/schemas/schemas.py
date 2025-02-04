"""Módulo que define os schemas do banco de dados"""

from pydantic import BaseModel


class Disciplina(BaseModel):
    """Classe que define um schema da Disciplina"""

    id_disciplina: str
    codigo: str
    nome: str
    feita: bool
    horarios: str
    depto: str
    turma: str
    periodo: str
    docente: str
    carga_horaria: str
    local: str

    class Config:
        """Classe de configuração"""

        from_attributes = True
