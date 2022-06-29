1. create directory and connect to github
2. setup virtual environment

    `python3 -m venv venv`

    `source venv/bin/activate`
    - will have to run source command every time you reopen terminal
3. install fastpi

    `python3 -m pip install fastapi[all]`

4. run app

    `uvicorn main:app --reload`

5. 