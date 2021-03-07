from src.container.ContainerNetwork import ContainerNetwork
from src.container.ContainerWrapper import ContainerWrapper


class DockerPublicNetwork:
    containers: list[ContainerWrapper]
    networks: list[ContainerNetwork]

    def __init__(self):
        self.containers=[]
        self.networks=[]

    def get_active(self):
        pass

    def to_output(self):
        pass
