```markdown
# Docker Instructions

This project includes Docker configuration to help you containerize and run your applications consistently across different environments.

## Running the Demo Script

The default setup includes a simple `demo.sh` script located in the `scripts/` directory. This script demonstrates how to use Docker with this template.

### Building the Docker Image

To build the Docker image, open a terminal in the project root directory and run:

```bash
docker build -t myapp:latest .
```

Alternatively, you can use the provided `Makefile`:

```bash
make docker-build
```

### Running the Docker Container

To run the Docker container and execute the `demo.sh` script:

```bash
docker run --rm myapp:latest
```

Or using the `Makefile`:

```bash
make docker-run
```

### Expected Output

The script will display the project directory structure and environment variables inside the Docker container.

## Adapting for Specific Programming Languages

To use Docker with your specific programming language (Python, C/C++, or x86/64 Assembly with NASM), you'll need to modify the `Dockerfile` and possibly other files. Below are instructions for each language.

### 1. Python

#### Modify the Dockerfile

Uncomment and modify the Python section in the `Dockerfile`:

```Dockerfile
# FROM python:3.9-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["python", "src/main.py"]
```

**Steps:**

1. **Set the Base Image:**

   Replace the base image line with:

   ```Dockerfile
   FROM python:3.9-slim
   ```

2. **Install Dependencies:**

   Ensure your Python dependencies are listed in `requirements.txt`.

3. **Copy Application Code:**

   The `COPY . .` instruction copies your application code into the container.

4. **Set the Command:**

   Update the `CMD` instruction to run your main Python script:

   ```Dockerfile
   CMD ["python", "src/main.py"]
   ```

#### Update Other Files

- **requirements.txt:**

  Create a `requirements.txt` file listing your Python dependencies.

- **Main Application:**

  Place your main Python script in `src/main.py`.

#### Remove or Update `demo.sh`

- Remove the `demo.sh` script if it's not needed.
- Update the `ENTRYPOINT` or `CMD` in the `Dockerfile` accordingly.

### 2. C/C++

#### Modify the Dockerfile

Uncomment and modify the C/C++ section in the `Dockerfile`:

```Dockerfile
# FROM gcc:latest
# WORKDIR /app
# COPY . .
# RUN gcc -o main src/main.c
# CMD ["./main"]
```

**Steps:**

1. **Set the Base Image:**

   Replace the base image line with:

   ```Dockerfile
   FROM gcc:latest
   ```

2. **Copy Source Code:**

   Ensure your source code is in the `src/` directory.

3. **Compile the Application:**

   The `RUN` instruction compiles your C/C++ program:

   ```Dockerfile
   RUN gcc -o main src/main.c
   ```

   Modify as needed for multiple source files or C++ (`g++`).

4. **Set the Command:**

   Update the `CMD` instruction to execute your compiled binary:

   ```Dockerfile
   CMD ["./main"]
   ```

#### Update Other Files

- **Main Application:**

  Place your main C/C++ source file in `src/main.c` or `src/main.cpp`.

#### Remove or Update `demo.sh`

- Remove the `demo.sh` script if it's not needed.
- Update the `ENTRYPOINT` or `CMD` in the `Dockerfile` accordingly.

### 3. x86/64 Assembly (NASM)

#### Modify the Dockerfile

Uncomment and modify the NASM section in the `Dockerfile`:

```Dockerfile
# FROM ubuntu:20.04
# RUN apt-get update && apt-get install -y nasm && rm -rf /var/lib/apt/lists/*
# WORKDIR /app
# COPY src/ ./src/
# RUN nasm -f elf64 src/main.asm -o main.o
# RUN ld -o main main.o
# CMD ["./main"]
```

**Steps:**

1. **Set the Base Image:**

   Replace the base image line with:

   ```Dockerfile
   FROM ubuntu:20.04
   ```

2. **Install NASM:**

   The `RUN` instruction installs NASM assembler.

3. **Copy Source Code:**

   Ensure your assembly source code is in the `src/` directory.

4. **Assemble and Link:**

   The `RUN` instructions assemble and link your program:

   ```Dockerfile
   RUN nasm -f elf64 src/main.asm -o main.o
   RUN ld -o main main.o
   ```

5. **Set the Command:**

   Update the `CMD` instruction to execute your assembled program:

   ```Dockerfile
   CMD ["./main"]
   ```

#### Update Other Files

- **Main Application:**

  Place your main assembly source file in `src/main.asm`.

#### Remove or Update `demo.sh`

- Remove the `demo.sh` script if it's not needed.
- Update the `ENTRYPOINT` or `CMD` in the `Dockerfile` accordingly.

## Additional Notes

- **Updating the Makefile:**

  Adjust the `Makefile` targets if necessary to match your build and run commands.

- **Dependencies:**

  Ensure all your application's dependencies are properly installed within the Docker image.

- **Exposing Ports:**

  If your application listens on a network port, use the `EXPOSE` instruction in the `Dockerfile` and map ports when running the container.

  ```Dockerfile
  EXPOSE 8080
  ```

- **Environment Variables:**

  Set environment variables using the `ENV` instruction in the `Dockerfile` or pass them at runtime.

  ```Dockerfile
  ENV ENV_VAR_NAME=value
  ```

- **Data Persistence:**

  Use Docker volumes to persist data outside the container.

## Using Docker Compose (Optional)

If your application requires multiple services (e.g., a web server and a database), you can use `docker-compose.yml` to manage them.

### Example `docker-compose.yml` for Python

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
    command: >
      python src/main.py
```

### Running with Docker Compose

```bash
docker-compose up
```

Or using the `Makefile`:

```bash
make docker-compose-up
```

## Cleaning Up

To stop and remove containers and images:

```bash
# Stop all running containers based on the image
docker stop $(docker ps -q --filter ancestor=myapp:latest)

# Remove stopped containers
docker rm $(docker ps -a -q --filter ancestor=myapp:latest)

# Remove the image
docker rmi myapp:latest
```

Or using the `Makefile`:

```bash
make docker-stop
make docker-clean
```

## Help and Resources

- **Docker Documentation:** [https://docs.docker.com/](https://docs.docker.com/)
- **Dockerfile Reference:** [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
- **Docker Compose Documentation:** [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

If you encounter any issues or have questions, please refer to the documentation or seek assistance from your instructor.
