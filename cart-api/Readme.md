docker build -t cart-api-docker .

docker run -h cartservice -d -p 5050:5000 cart-api-docker