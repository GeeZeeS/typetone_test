import os


class Config:
    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DATABASE_URL: str = os.getenv('DATABASE_URL')

