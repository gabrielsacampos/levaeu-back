import os
import pandas as pd
from src.database.settings.connection import DBConnectionHandler
from sqlalchemy import text
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from termcolor import colored


class Seeder(DBConnectionHandler):
    def __init__(self) -> None:
        super().__init__()

        self.__seeds_path = os.path.dirname(os.path.realpath(__file__)) + '/seeds.xlsx'
        sheets_names = pd.ExcelFile(self.__seeds_path).sheet_names

        db_table_names = inspect(self.engine).get_table_names()
        self.tables_to_seed = [table for table in sheets_names if table in db_table_names]

    def drop_tables(self, tables_list: list):
        with self.engine.connect() as connection:
            for table in tables_list:
                connection.execute(text("PRAGMA foreign_keys=OFF;"))
                connection.execute(text(f"DROP TABLE IF EXISTS {table};"))
                print(f"Table {table} dropped")

    def seed(self):
        self.drop_tables(self.tables_to_seed)
        self.settup_database()
        for table in self.tables_to_seed:
            seeds = pd.read_excel(self.__seeds_path, sheet_name=table)

            try:
                seeds.to_sql(table, con=self.engine, if_exists='append', index=False)
                print(colored(f"Table {table} seeded", "green"))
            except IntegrityError:
                print(colored(f"Error while seeding {table} data. IntegrityError", "red"))
                raise Exception(IntegrityError)
            except Exception as error:
                raise Exception(colored(f"Error while seeding {table} data. {error}", "red"))



Seeder().seed()
