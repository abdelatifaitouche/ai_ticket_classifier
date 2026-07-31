from src.infra.db.engine import engine
from sqlalchemy.orm import sessionmaker, Session


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    with SessionLocal() as session:
        try:
            yield session
        except:
            session.rollback()
        finally:
            session.close()
