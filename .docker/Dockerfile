# Use a minimal base image with bash installed
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache bash coreutils tree

# Set the working directory
WORKDIR /app

# Copy the scripts directory into the container
COPY scripts/ ./scripts/

# Set execute permission on the script
RUN chmod +x ./scripts/demo.sh

# Set the entrypoint to run the demo script
ENTRYPOINT ["./scripts/demo.sh"]

## --------------------------------------------------------
## Examples for specific languages (uncomment and modify as needed)

## Example for Python
# FROM python:3.9-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["python", "src/main.py"]

## Example for C/C++
# FROM gcc:latest
# WORKDIR /app
# COPY . .
# RUN gcc -o main src/main.c
# CMD ["./main"]

## Example for x86/64 Assembly (NASM)
# FROM ubuntu:20.04
# RUN apt-get update && apt-get install -y nasm && rm -rf /var/lib/apt/lists/*
# WORKDIR /app
# COPY src/ ./src/
# RUN nasm -f elf64 src/main.asm -o main.o
# RUN ld -o main main.o
# CMD ["./main"]

