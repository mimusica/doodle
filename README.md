# doodle
Technical challange

## Local
Install a virtual environment in the current working directory:
```bash
python3 -m venv .venv
```
### Test the application on your local machine:
```bash
for m in GET POST PUT DELETE CONNECT OPTIONS TRACE PATCH; do curl -X $m localhost:8080; done
```

## Docker:
### Build a local docker image
```bash
docker build -t challenge:latest .
```

### pull the remote docker image
#TODO: add github url
```bash
docker pull <ghub url> challenge:latest
```

### Test the application:
[Test the application][Test the application on your local machine]:

## Kubernetes
