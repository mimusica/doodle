[![Push to GHCR](https://github.com/mimusica/doodle/actions/workflows/main.yml/badge.svg)](https://github.com/mimusica/doodle/actions/workflows/main.yml)

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
docker pull ghcr.io/mimusica/doodle-challenge:latest
```

### Test the application:
[Test the application][Test the application on your local machine]:

## Kubernetes
### cluster IP
```bash
kubectl apply -f deployment-clusterip.yml
```

### Loadbalancer
```bash
kubectl apply -f deployment-loadbalancer.yml
```


## Important
Don't forget to add an entry in your local hosts file or add a dns record pointing to the correct IP address.
