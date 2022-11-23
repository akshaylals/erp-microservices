```$ docker build --tag products-api-docker .```

```$ docker run -d -h productsservice --name=products-service --network=erpnet products-api-docker```
