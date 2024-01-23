import os


class Config:
    DATABASE_URL: str = os.getenv('DATABASE_URL')
