from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Interior AI Platform"

    DATABASE_URL: str = (
        "postgresql://postgres:postgres@localhost:5432/interior_ai"
    )


settings = Settings()