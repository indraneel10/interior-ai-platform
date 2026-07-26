from sqlalchemy import create_engine, text
from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:
    print(conn.execute(text("SELECT version();")).fetchone())
