### Project information
This is the solution for test task of abz.agency for Python Developer position.
Full description and requirements are described in ```Test Task Junior Python Developer.pdf```
The list of already accomplished task parts is given in ```Issues``` tab of this repository.


#### Create and setup of Postgre DB for project:
1. Run Postgre server, in command line execute command:
    ```bash
    CREATE DATABASE test_db;
    ```
2. To run the migrations initialize Alembic:
    ```bash
    $ cd abz.agency.test_task/server/db
    $ PYTHONPATH=$PWD/../../ python migration.py db init
    ```
3. To create the first migration run the migrate command:
    ```bash
    $ PYTHONPATH=$PWD/../../ python migration.py db migrate
    ```
4. Apply the upgrades to the database:
    ```bash
    $ PYTHONPATH=$PWD/../../ python migration.py db upgrade
    ```
    At this step the database is created and ready for data storage.
5. _Optional: Fill test database with fake data for testing purposes. To insert 55k+ random records with 5-level nesting run script_ ```
    test_db_setup.py```


#### Package requirements:
>* Python 3.7
>* flask
>* flask_script
>* flask_migrate
>* flask_sqlalchemy
>* psycopg2
>* faker

#### Server start:
1. At first, make settings for your Postgre DB in ```/server/__init__.py```
2. To start server run script ```start_server.py```
   
   The Tree view of employees is located at:
   ```http://127.0.0.1:5000/```
   
   The overall list of employees with all available information is located at:
   ```http://127.0.0.1:5000/list/```
   
#### CRUD, search and sorting at server:
To execute CRUD operations you need to go to the overall list of employees (see above).
* To CREATE new record press ```Create new record``` button at the top-left corner of the page.
* To UPDATE existing record press related ```update``` button near Username in the record you would like to change.
* To DELETE existing record press related ```delete``` button near Username in the record you would like to delete.
* To perform SEARCH of record input corresponding data at search inputs on top of the table.
* To SORT records press corresponding buttons on top of the table.
* By default the table outputs first 100 sorted records. To see next records, press ```Load next``` button on the bottom of the table.
