from sqlalchemy import create_engine, text
from app.config.settings import settings

print("DATABASE_URL:", settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL, echo=True)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_user, current_database(), version();"))
        print(result.fetchone())
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Connection failed:")
    print(type(e).__name__)
    print(e)
