# Excercism Python Track with Docker

Using a docker image to run exercism to keep it simple and not let it affect the tooling on my machine.

The image is based on python:3-alpine, with the following modifications:
 * `bash` is installed. 
 * `excercism` is installed from source. 
 * requried pip packages (`docker/requirements.txt`) are installed. 

## 1. Run

This runs the docker image in an interactive mode. `code` is mounted at `/root/excercism/python`

```
./run.sh
```

## 2. Building Docker Image

Run the following command in `docker` folder. Copy the token from [https://exercism.io/my/settings](https://exercism.io/my/settings) link

```
docker build -t ss-python --build-arg token="XXXX-XXXX" .
```
