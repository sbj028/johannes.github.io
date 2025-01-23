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

## Backend code is located in file `app.py`

# Set up Doppler for Secret Management: 
1. Run `sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | sudo gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | sudo tee /etc/apt/sources.list.d/doppler-cli.list
sudo apt-get update && sudo apt-get install doppler` for Ubuntu > 22.04 

2. Check that doppler is installed `doppler --version` 

3. Log in and authenticate in terminal by running `doppler login` and copy the code in the terminal to the browser. 

4. Go to the Doppler Dashboard and create a new project.

3. Run doppler (in environment) `doppler run -- python app.py` 



