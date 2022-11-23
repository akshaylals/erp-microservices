```$ docker build -t cart-api-docker .```

```$ docker run --network=erpnet --name=cart-service -h cartservice -d cart-api-docker```