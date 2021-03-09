from src.container.model.ContainerNetwork import ContainerNetwork
from src.container.model.ContainerWrapper import ContainerWrapper


class ContainerCluster:
    gateway: ContainerWrapper
    containers: list[ContainerWrapper]
    network: ContainerNetwork

    def __init__(self):
        self.containers = []
