import os
import pandas as pd
from src.database.settings.connection import connection_handler
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from termcolor import colored

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path + '/seeds.xlsx')


users_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='users')
establishments_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='establishments')
establishment_types_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='establishment_types')
ratings_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='ratings')  
user_categories_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='users_categories')

with connection_handler as database:
        engine = database.get_engine()
        
        try:
            user_categories_df.to_sql('user_categories', con=engine, if_exists='append', index=False)
        except IntegrityError:
            raise Exception(colored("Error while seeding user_category data. Some user_category already exists", "red"))
        
        try:
            users_df.to_sql('users', con=engine, if_exists='append', index=False)
        except IntegrityError:
            raise Exception(colored("Error while seeding users data. Some user already exists.", "red"))

        try:
            establishment_types_df.to_sql('establishment_types', con=engine, if_exists='append', index=False)
        except IntegrityError:
            raise Exception(colored("Error while seeding users data. Some establishment_type already exists.", "red"))
        
        try:
            establishments_df.to_sql('establishments', con=engine, if_exists='append', index=False)

        except IntegrityError:
            raise Exception(colored("Error while seeding establishments data. Some establishment already exists or not found id_type | id_sponsor.", "red"))
        
        try:
            ratings_df.to_sql('ratings', con=engine, if_exists='append', index=False)
        except IntegrityError:
            raise Exception(colored("Error while seeding ratings data. Some rating already exists or not found id_establishment or id_user.", "red"))
