# PRA3 TDD and Deploying Web Applications (Natalie)

Following instructions based on (https://github.com/shuruizUofT/flaskr-tdd)[https://github.com/shuruizUofT/flaskr-tdd].

### Python Setup
```bash
# install python3-venv package
sudo apt-get install python3-venv

# create a virtual environment named venv
python3 -m venv env

# activate the virtual environment
source env/bin/activate

# install relevant packages using pip
pip install -r requirements.txt
```

Run the app:
```bash
FLASK_APP=project/app.py python -m flask run -p 5001
```

Run tests:
```bash
python -m pytest
```

Set up Environment Variables

Needed for step [Connect the database to the Flaskr-tdd project](https://github.com/shuruizUofT/flaskr-tdd?tab=readme-ov-file#connect-the-database-to-the-flaskr-tdd-project)
```bash
export FLASK_APP=project/app.py
export DATABASE_URL="the value of the external database URL you copied earlier"

flask shell
```