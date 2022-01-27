from src.ORM_Utils.ORM_Class import *


class DatabaseORM(DatabaseConnection, MainTable):
    def __init__(self):
        self.metadata = MetaData()
        self.main_table = MainTable.__table__

        MainTable.__init__(self)
        DatabaseConnection.__init__(self)

    def create_tables(self):
        self.main_table.create()

    def show_tables(self):
        info = self.session.execute(self.main_table.select()).fetchall()
        return info

    def insert_tables(self) -> None:
        ins = [{'first_name': 'Ilya', 'last_name': 'Loh'}]
        ins2 = [{'first_name': 'Vadim', 'last_name': 'Demon'}]

        for insertion in [ins, ins2]:
            self.session.execute(self.main_table.insert(), insertion)

    def delete_tables(self):
        self.main_table.drop()
