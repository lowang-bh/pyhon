#!/usr/bin/env python
import docker


client = docker.from_env()
print(client.containers.list(all=True))
print(client.images.list(all=True))
