import logging
import os

from docker import DockerClient
from os import path

from src.container.ContainerWrapper import ContainerWrapper
from src.render.OutputHandler import OutputHandler

logger = logging.getLogger(__name__)


class DockerHandler:
    client: DockerClient

    def __init__(self, client: DockerClient, output_handler: OutputHandler):
        self.client = client
        self.output_handler = output_handler

    def init(self):
        self.refresh_container(event=None)

    def handle(self, event):
        action = event['Action']
        if action == 'start' or action == 'stop':
            self.refresh_container(event)

    def refresh_container(self, event):
        logger.debug("###### REFRESH START ############################")
        output_context = {"containers": []}
        containers = self.client.containers.list(all=True)
        for container in containers:
            container_wrap = ContainerWrapper(container)
            if container_wrap.is_running():
                logger.debug("RUNNING: " + container_wrap.id())
                if container_wrap.is_relevant():
                    logger.info("FOUND RELEVANT RUNNING CONTAINER id:%s", container_wrap.id())
                    output_context["containers"].append({"__raw__": container.attrs, "id": container_wrap.id()})
                logger.debug(container_wrap.id())
        self.output_handler.run(output_context)
        logger.debug("###### REFRESH END ############################")
