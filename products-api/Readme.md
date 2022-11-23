```$ docker build --tag products-api-docker .```

```$ docker run -it -d -h productsservice -p 5060:3000 --network=erpnet products-api-docker```
