from sqlalchemy import Column
from clickhouse_sqlalchemy import get_declarative_base, types, engines
from src.Database_Utils.DB_Connect import *

DBClass = DatabaseConnection()

Base = get_declarative_base(metadata=DBClass.metadata)


class MainTable(Base):
    id = Column(types.Int32, primary_key=True)
    first_name = Column(types.String)
    last_name = Column(types.String)

    __table_args__ = (
        engines.Memory(),
    )


