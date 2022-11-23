```$ docker build -t reverseproxy .```

```$ docker run -d -p 5000:5000 --network=erpnet --name=reverse-proxy reverseproxy```