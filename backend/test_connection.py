from sqlalchemy import text

from app.database.database import engine


try:

    with engine.connect() as conn:

        result = conn.execute(text("SELECT version();"))

        print(result.fetchone())

        print("\n")
        print("Database Connected Successfully")

except Exception as e:

    print(e)
