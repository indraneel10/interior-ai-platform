from app.database.base import Base
from app.database.database import engine

import app.models

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("All tables created successfully.")
