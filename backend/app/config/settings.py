from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Interior AI Platform"

    DATABASE_URL: str = "postgresql://postgres:Risind123@@localhost:5432/interior_ai"

    OPENAI_API_KEY: str = ""

    EXOTEL_API_KEY: str = ""

    EXOTEL_API_TOKEN: str = ""

    EXOTEL_SID: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
