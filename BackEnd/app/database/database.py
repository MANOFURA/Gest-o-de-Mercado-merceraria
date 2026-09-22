from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Caminho do banco de dados
DATABASE_URL = "sqlite:///./mercearia.db"

# Criação da conexão
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criador de sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe base dos modelos
Base = declarative_base()