from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco (SQLite local)
DATABASE_URL = "sqlite:///./brokerlab.db"

# engine = conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário para SQLite
)

# sessão do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# base para os modelos
Base = declarative_base()


# função para pegar conexão (usada na API depois)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
