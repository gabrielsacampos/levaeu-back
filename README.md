# LevaEu

As its core, LevaEu is a platform that connects people with establishments, providing families with a relaxing and funny day filled with good memories.
The project is currently in the initial phase of building a Minimum Viable Product (MVP) as part of the postgraduate Software Engineering sprint at PUC-RJ.

The architecture of this project follows the MVC pattern, separating the frontend and backend into different repositories. You can check the frontend repository at this link [__comming soon__].

#### storage.sqlite3
   > Populated sqlite database with fake data

#### seeds 
   > When needed, we can seed our database from _./seeds/seeder.py_
    It runs a pandas to **DROP** each table and seed them with fake data from xslx file at _.seed/seed.xlsx_
     
### src
#### - models
###### -- entities
   > Building database schema

###### -- repository
   > Implements methods to database

#### - http
###### -- controllers
   > Routing our application
#### - services
   > Implements methods to handle request from controllers



ModuleNotFoundError:
    
    export PYTHONPATH=./:$PYTHONPATH


Instalation:
    1-
    
    $ git clone https://github.com/gabrielsacampos/levaeu-back.git
    
2 - Install requirements
    
    $ pip install -r requirements.txt

4 - testing

    $ pytest -s -v

3 - running application
    
    $ python app.py
