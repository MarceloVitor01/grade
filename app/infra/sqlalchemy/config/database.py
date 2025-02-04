"""Módulo de conexão com o banco de dados"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL = 'postgresql://postgres:dnQQALREuOpO5fcz@generously-trusting-kangaroo.data-1.use1.tembo.io:5432/grid'

engine = create_engine(URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def cria_banco():
    """Cria o banco de dados"""

    Base.metadata.create_all(bind=engine)


def get_session():
    """Retorna uma sessão do banco de dados"""

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()
