import os
import pandas as pd
from src.models.database.settings.connection import connection_handler
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from termcolor import colored

dir_path = os.path.dirname(os.path.realpath(__file__))


with connection_handler as database:
    engine = database.get_engine()
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    print(colored(f"Started seedings tables: {table_names}", "green"))

    for table_name in table_names:
        try:
            database.execute(f"TRUNCATE TABLE {table_name} CASCADE;")
        except Exception as error:
            print(error)
            raise Exception(colored(f"Error while truncating table {table_name}", "red"))
        
        table_seeds = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name=table_name)

        try:
            table_seeds.to_sql(table_name, con=engine, if_exists='append', index=False)
            print(colored(f"Table {table_name} seeded", "green"))
        except IntegrityError:
            raise Exception(colored(f"Error while seeding {table_name} data. Some data already exists", "red"))
        except Exception as error:
            raise Exception(colored(f"Error while seeding {table_name} data. {error}", "red"))
        
        
      