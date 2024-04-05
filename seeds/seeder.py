import os

from sqlalchemyseed import load_entities_from_json, Seeder
from src.database.settings.connection import connection_handler

dir_path = os.path.dirname(os.path.realpath(__file__))
seeds_path = os.path.join(dir_path, 'seeds.json')

seeds = load_entities_from_json(seeds_path)

with connection_handler as database:
    seeder = Seeder(database.session)

seeder.seed(seeds)

connection_handler.session.commit()
