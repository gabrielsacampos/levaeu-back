import os
import pandas as pd
from src.database.settings.connection import connection_handler

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path + '/seeds.xlsx')


users_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='users')
establishments_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='establishments')
establishment_types_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='establishment_types')
ratings_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='ratings')  
user_categories_df = pd.read_excel(dir_path + '/seeds.xlsx', sheet_name='users_categories')

with connection_handler as database:
    engine = database.get_engine()
    user_categories_df.to_sql('users_categories', con=engine, if_exists='replace', index=False)
    users_df.to_sql('users', con=engine, if_exists='replace', index=False)
    establishment_types_df.to_sql('establishment_types', con=engine, if_exists='replace', index=False)
    establishments_df.to_sql('establishments', con=engine, if_exists='replace', index=False)
    ratings_df.to_sql('ratings', con=engine, if_exists='replace', index=False)

