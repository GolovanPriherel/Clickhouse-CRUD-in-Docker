from sqlalchemy import create_engine, MetaData
from clickhouse_sqlalchemy import make_session

from src.Other_Utils.Directory_Utils import *


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(clickhouse_dialect)
        self.session = make_session(self.engine)
        self.metadata = MetaData(bind=self.engine)
