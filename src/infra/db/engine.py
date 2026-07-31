from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///test_db.db"

engine = create_engine(DATABASE_URL, echo=True)
