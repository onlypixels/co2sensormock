# co2sensormock - mocking CO2 sensor API

## Virtual environment
Worth creating a virtual environment"
```
python3 -m venv venv
```
To activate:
```
. venv/bin/activate
```
Check the Python version:
```
python --version
```

## Install
```
pip install flask
pip install flask-cors
```

## Run
The below command will run it so it can be accessed by other machines on the network:

```
export FLASK_APP=application
flask run --host=0.0.0.0
```
