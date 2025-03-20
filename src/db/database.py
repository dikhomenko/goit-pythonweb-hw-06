import os
from sqlalchemy import create_engine, MetaData

# db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/database.db'))
# engine = create_engine(f'sqlite:///{db_path}', echo=True)

engine = create_engine(
    "postgresql://postgres:567234@localhost:5432/mydatabase", echo=True
)


metadata = MetaData()


def init_db():
    metadata.create_all(bind=engine)
