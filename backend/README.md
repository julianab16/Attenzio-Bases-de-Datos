## Steps run the backend without Docker


### 1. Create and activate python environment

Inside backend folder:

```
# Create the virtual environment
python -m venv env 
```

or

```
# Create the virtual environment
virtualenv -p python3 env
```

```
# Activate the virtual environment (Linux/Mac)
source env/bin/activate
```

```
# Activate the virtual environment (Windows)
env\Scripts\activate
```

### 2. Install dependencies

```
pip install -r requirements.txt

### 1. Build docker image

Inside backend folder:

```
docker build -t jmb/attenzio_backend .

```
### 2. Run backend within Docker container

```
docker run --name attenzio_backend -p 0.0.0.0:8000:8000 jmb/attenzio_backend
```

