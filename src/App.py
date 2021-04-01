import logging
import os
from os import path

import docker
from docker import DockerClient
from jinja2 import Environment, FileSystemLoader

from src.container.DockerHandler import DockerHandler
from src.render.OutputHandler import OutputHandler

logger = logging.getLogger(__name__)


class App:
    client: DockerClient
    dockerHandler: DockerHandler
    j2_env: Environment

    def __init__(self):
        self.data = []
        self.client = docker.from_env()
        self.j2_env = Environment(
            loader=FileSystemLoader(
                searchpath=os.path.join(
                    os.path.dirname(os.path.dirname(__file__)),
                    "config"
                )
            )
        )
        self.dockerHandler = DockerHandler(
            self.client,
            OutputHandler(
                self.j2_env,
                path.join(path.dirname(path.dirname(__file__)), "config"),
                path.join(path.dirname(path.dirname(__file__)), "output")
            )
        )

    def run_once(self):
        logger.info("Started")
        self.dockerHandler.init()

    def run_as_daemon(self):
        logger.info("Started")
        self.dockerHandler.init()
        for event in self.client.events(decode=True):
            self.dockerHandler.handle(event)
