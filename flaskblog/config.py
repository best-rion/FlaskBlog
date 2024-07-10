from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') #example : 'rljr4yawodg4f4f6fovbw2y8cni8889u'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') #example : 'sqlite:///example.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('USERNAME') #example : 'example@demo.com'
    MAIL_PASSWORD = os.getenv('PASSWORD') #example : '44gg 806q eoq3 jjoh'
