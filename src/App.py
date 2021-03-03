import logging

import docker
from docker import DockerClient

from src.DockerHandler import DockerHandler

logger = logging.getLogger(__name__)


class App:
    client: DockerClient
    dockerHandler: DockerHandler

    def __init__(self):
        self.data = []

    def run(self):
        self.client = docker.from_env()
        self.dockerHandler = DockerHandler(self.client)
        logger.info("Started")
        self.dockerHandler.init()
        for event in self.client.events(decode=True):
            self.dockerHandler.handle(event)
