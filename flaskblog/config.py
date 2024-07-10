from dotenv import load_dotenv
import os

class Config:
    SECRET_KEY = '2b2a6e492a824a6d844b9af527c9b415'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    load_dotenv()
    MAIL_USERNAME = os.getenv('USERNAME')
    MAIL_PASSWORD = os.getenv('PASSWORD')
