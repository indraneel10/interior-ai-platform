from sqlalchemy import create_engine, text
from app.config.settings import settings

print("DATABASE_URL =", settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:
    print(conn.execute(text("SELECT version();")).fetchone())
