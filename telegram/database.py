from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from environs import Env

env = Env()
env.read_env()

NAME = env('DB_NAME')
USER = env('DB_USER')
PASSWORD = env('DB_PASSWORD')
HOST = env('DB_HOST')
PORT = env('DB_PORT')
DB_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'

engine = create_engine(DB_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
