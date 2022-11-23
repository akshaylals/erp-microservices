```$ docker build -t reverseproxy .```

```$ docker run -it -d -p 5000:5000 --network=erpnet reverseproxy```