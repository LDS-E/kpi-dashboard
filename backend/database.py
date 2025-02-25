from sqlalchemy import text
from .core.config import engine, SessionLocal  # Importa engine e SessionLocal
from sqlalchemy.orm import declarative_base


Base = declarative_base() 


def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print("❌ Erro ao conectar ao banco de dados:", e)
    finally:
        db.close()

test_connection()

__all__ = ["engine", "SessionLocal", "test_connection", "Base"]