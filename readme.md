1. create directory and connect to github
2. setup virtual environment

    `python3 -m venv venv`

    `source venv/bin/activate`
    - will have to run source command every time you reopen terminal
3. install fastpi

    `python3 -m pip install fastapi[all]`

4. run app

    `uvicorn main:app --reload`

5. create app package
    - new folder called app
    - move main.py into app
    - new command is:
    
        `uvicorn app.main:app --reload`

5. install postgress
    - had to change install location to avoid issues apparently related to MacOS security features


    installed with homebrew...

        `brew install postgres`
        
    some notes: 
        To migrate existing data from a previous major version of PostgreSQL run:
        brew postgresql-upgrade-database

        This formula has created a default database cluster with:
        initdb --locale=C -E UTF-8 /usr/local/var/postgres
        For more details, read:
        https://www.postgresql.org/docs/14/app-initdb.html

        To restart postgresql after an upgrade:
        brew services restart postgresql
        Or, if you don't want/need a background service you can just run:
        /usr/local/opt/postgresql/bin/postgres -D /usr/local/var/postgres
        ==> Summary
        🍺  /usr/local/Cellar/postgresql/14.4: 3,307 files, 45.5MB
        ==> Running `brew cleanup postgresql`...
        Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
        Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
        ==> Caveats
        ==> postgresql
        To migrate existing data from a previous major version of PostgreSQL run:
        brew postgresql-upgrade-database

        This formula has created a default database cluster with:
        initdb --locale=C -E UTF-8 /usr/local/var/postgres
        For more details, read:
        https://www.postgresql.org/docs/14/app-initdb.html

        To restart postgresql after an upgrade:
        brew services restart postgresql
        Or, if you don't want/need a background service you can just run:
        /usr/local/opt/postgresql/bin/postgres -D /usr/local/var/postgres

    Following this blog... https://www.mariadcampbell.com/blog/installing-pgadmin-only-after-installing-postgresql-with-homebrew-part-2/

        `brew services start postgres`
        `createdb `whoami``
        `createuser -s postgres`
        `psql`
        `\du`
        `ALTER USER postgres WITH PASSWORD 'password';`
        `\q`
        `psql -U postgres`

6. Install psycopg2
    - Needed to install Xcode Command Line Tools
        - Computer is old... had to download from Apple Developer Portal... it worked!
    - For some reason, am able to connect to DB with incorrect password
        - perhaps check here if it becomes an issue in the future https://www.peterbe.com/plog/connecting-with-psycopg2-without-a-username-and-password

7. Install sqlalchemy

    `pip install sqlalchemy`

8. Install passlib

    `pip install "passlib[bcrypt]"`

9. Install python-jose

    `pip install python-jose[cryptography]`

10. Install alembic

    `pip install alembic`

    - Create alembic directory

        `alembic init [directory name]`
    - Create revision file
    
        `alembic revision -m "message"`
    - Implement change(revision) to database

        `alembic upgrade [revision number]`
    - View latest revision number

        `alembic heads`
    - Alembic autogenerate database items to match sqlalchemy metadata

        `alembic revision --autogenerate`

11. Create heroku account

12. Install heroku

    `brew tap heroku/brew && brew install heroku`
    `heroku login`
    `heroku create [app-name]`

13. specify python version

    - create runtime.txt
    - add python version to it: `python-3.9.131


14. Move code to heroku

    `git push heroku master`

15. Create postgres database on heroku

    `heroku addons:create heroku-postgresql:hobby-dev`

16. restart heroku app

    `heroku ps:restart`

17. Run alembic on heroku server

    `heroku run [command]`
    `heroku run "alembic upgrade head"`