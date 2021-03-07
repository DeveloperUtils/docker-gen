from src.container.ContainerNetwork import ContainerNetwork
from src.container.ContainerWrapper import ContainerWrapper


class DockerPublicNetwork:
    containers: dict[ContainerWrapper]
    networks: dict[ContainerNetwork]

    def __init__(self):
        self.containers = {}
        self.networks = {}

    def add_container(self, container: ContainerWrapper):
        self.containers[container.id()] = container
