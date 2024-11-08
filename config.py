import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost:5432/GE_facul')
    SQLALCHEMY_TRACK_MODIFICATIONS = True