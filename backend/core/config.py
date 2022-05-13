from decouple import config


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = config('POSTGRES_USER')
    POSTGRES_PASSWORD: str = config('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = config('POSTGRES_SERVER')
    POSTGRES_PORT: str = config('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = config('POSTGRES_DB', 'tdd')
    DATABASE_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
