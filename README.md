# marxsaid
Marxsaid.com client

# Build the docker image
docker build --rm -t marxsaid:1.0 -f DockerFile .

# Run the image you just built
docker run --rm -ti marxsaid:1.0 python marx_client.py
