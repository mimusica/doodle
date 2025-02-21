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
for m in GET POST PUT DELETE; do curl -X $m localhost:8080; done
```

## Docker:
### Build a local docker image
```bash
docker build -t challenge:latest .
```

### pull the remote docker image
```bash
docker pull ghcr.io/mimusica/doodle-challenge:latest
```

### Test the application:
```bash
for m in GET POST PUT DELETE; do curl -X $m localhost:8080; done
```

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
<br><br>
Currently the ingress is configured to use "hello.local"<br>
testing locally with minikube:<br>
e.g.:
```angular2html
192.168.49.2     hello.local
```

### Test the application with minikube:
```bash
for m in GET POST PUT DELETE; do curl -X $m hello.local; done
```
