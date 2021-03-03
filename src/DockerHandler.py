import logging

from docker import DockerClient

from src.ContainerWrapper import ContainerWrapper

logger = logging.getLogger(__name__)


class DockerHandler:
    client: DockerClient

    def __init__(self, client: DockerClient):
        self.client = client

    def init(self):
        self.refresh_container(event=None)

    def handle(self, event):
        action = event['Action']
        if action == 'start' or action == 'stop':
            self.refresh_container(event)

    def refresh_container(self, event):
        logger.debug("###### REFRESH START ############################")
        containers = self.client.containers.list(all=True)
        for container in containers:
            container_wrap = ContainerWrapper(container)
            if container_wrap.is_running():
                logger.debug("RUNNING: " + container_wrap.id())
                if container_wrap.is_relevant():
                    logger.info("FOUND RELEVANT RUNNING CONTAINER id:%s", container_wrap.id())
                logger.debug(container_wrap.id())
        logger.debug("###### REFRESH END ############################")
