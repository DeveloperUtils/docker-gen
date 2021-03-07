from docker.models.containers import Container

from src.container.ContainerConfig import ContainerConfig
from src.container.ContainerNetwork import ContainerNetwork


class ContainerWrapper:

    def __init__(self, container_info: Container):
        self.raw: dict = container_info.attrs
        self.wrapped: Container = container_info
        self.config: ContainerConfig = ContainerConfig(self.wrapped.labels)
        self._networks: dict[ContainerNetwork] = self.get_all_networks(container_info.attrs)

    def is_running(self) -> bool:
        return self.wrapped.status == 'running'

    def id(self) -> str:
        return self.wrapped.id

    def name(self) -> str:
        return self.wrapped.name

    def networks(self) -> dict[ContainerNetwork]:
        return self._networks

    def is_relevant(self) -> bool:
        return self.config.is_enabled()

    @staticmethod
    def get_all_networks(attrs: dict) -> dict[ContainerNetwork]:
        networks: dict = attrs["NetworkSettings"]["Networks"]
        ret: dict = {}
        for network_id, network in networks.items():
            ret[network_id] = ContainerNetwork(network_id, network)
        return ret

    def exposed_ip4_address(self) -> str:
        first_network: ContainerNetwork = list(self._networks.values())[0]
        return first_network.get_ip4_address()

    def exposed_ip4_port(self):
        return "80"
