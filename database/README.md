### 3. Build database image

inside database folder:

```
docker build -t jmb/attenzio .
```

### 4. Run server with postgres

```
docker run --name attenzio -p 0.0.0.0:5432:5432 -e POSTGRES_PASSWORD=aP4sw0rd jmb/attenzio
```


### Run integrate with dockercompose

Under development
