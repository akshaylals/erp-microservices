docker build --tag cart-api-docker .

docker run -h cartservice -d -p 5000:5000 cart-api-docker