### 1. Build docker image

Inside backend folder:

```
docker build -t jmb/attenzio_backend .

```
### 2. Run backend within Docker container

```
docker run --name attenzio_backend -p 0.0.0.0:8000:8000 jmb/attenzio_backend
```

