docker build -t cart-api-docker .

docker run --network=erpnet -h cartservice -d -p 5050:5000 cart-api-docker