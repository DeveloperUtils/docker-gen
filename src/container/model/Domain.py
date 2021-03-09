from typing import Optional

from src.container.model.ContainerCluster import ContainerCluster
from src.container.model.ContainerWrapper import ContainerWrapper


class DockerPublicNetwork:
    containers: dict[str, ContainerWrapper]

    def __init__(self):
        self.containers = {}
        self.networks = {}

    def add_container(self, container: ContainerWrapper):
        self.containers[container.id()] = container

    def get_outbound_network(self) -> ContainerCluster:
        ret = ContainerCluster()
        ret.gateway = self.get_reverse_proxy()
        ret.containers = self.get_containers_served_by(ret.gateway)
        return ret

    def get_reverse_proxy(self) -> Optional[ContainerWrapper]:
        for container in self.containers.values():
            if container.is_public_gateway():
                return container
        return None

    def get_containers_served_by(self, reverse_proxy: ContainerWrapper) -> list[ContainerWrapper]:
        ret: list[ContainerWrapper] = []
        for container in self.containers.values():
            if container.has_connection_to(reverse_proxy) and not container.is_public_gateway():
                ret.append(container)

        return ret
