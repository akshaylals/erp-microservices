```$ docker build --tag products-api-docker .```

```$ docker run -d -h productsservice -p 5060:4000 --network=erpnet products-api-docker```
