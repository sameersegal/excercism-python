#!/bin/bash
docker rm python-workspace
docker run  -it --entrypoint bash -v "$PWD/code:/root/exercism/python" --name python-workspace ss-python
