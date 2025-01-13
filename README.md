# johannes.github.io

# Backend setup for webpage registration with Flask and MySQL: 

## Setting Up the Database
1. Install MySQL or use a hosted database.
2. Create a database named `event_registration`.
3. Run the `schema.sql` file to set up the required tables.


## Create a virtual environment 
```
python -m venv regenv
source regenv/bin/activate # Linux/macOS
```

## Install necessary packages to the virtual environment: 

#### Possibly update `pip`: 
pip install --upgrade pip 

### Flask and dependencies: 
`pip install flask flask-mysql flask-bcrypt flask-cors`


## Configuration files
An example template for the credentials of the environment can be found in the file `.env.example`  


