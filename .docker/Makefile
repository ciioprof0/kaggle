# Makefile for Docker operations

# Variables
IMAGE_NAME = myapp
TAG = latest
# PORT variable is optional here since demo.sh doesn't use it
# PORT = 5000

# Build the Docker image
docker-build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Run the Docker container (no port mapping needed for demo.sh)
docker-run:
	docker run --rm $(IMAGE_NAME):$(TAG)

# Stop all running containers (if any)
docker-stop:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME):$(TAG)) || true

# Remove all stopped containers
docker-clean:
	docker rm $$(docker ps -a -q --filter ancestor=$(IMAGE_NAME):$(TAG)) || true

# Run Docker Compose (if using docker-compose.yml)
docker-compose-up:
	docker-compose up

docker-compose-down:
	docker-compose down

# --------------------------------------------------------
# Examples for specific languages (uncomment and modify as needed)

# Example for Python
# Set the port your application listens on
# PORT = 5000

# docker-run:
# 	docker run -p $(PORT):$(PORT) --rm $(IMAGE_NAME):$(TAG)

# Example for C/C++
# docker-run:
# 	docker run --rm $(IMAGE_NAME):$(TAG)

# Example for x86/64 Assembly (NASM)
# docker-run:
# 	docker run --rm $(IMAGE_NAME):$(TAG)
