from docker.models.containers import Container

from src.container.model.ContainerConfig import ContainerConfig
from src.container.model.ContainerNetwork import ContainerNetwork, NetworkSettings


class ContainerWrapper:

    def __init__(self, container_info: Container):
        self.raw: dict = container_info.attrs
        self.wrapped: Container = container_info
        self.config: ContainerConfig = ContainerConfig(self.wrapped.labels)
        self.network: NetworkSettings = NetworkSettings(self.raw["NetworkSettings"])

    def is_running(self) -> bool:
        return self.wrapped.status == 'running'

    def id(self) -> str:
        return self.wrapped.id

    def name(self) -> str:
        if self.wrapped.name:
            return self.wrapped.name
        else:
            return self.id()

    def is_relevant(self) -> bool:
        return self.config.is_enabled() and (self.is_public_gateway() or self.config.is_configured())

    def is_public_gateway(self) -> bool:
        return self.config.is_public_gateway()

    def has_connection_to(self, container) -> bool:
        """

        :type container: ContainerWrapper
        """
        return container.network.has_connection_to(self.network)

    def get_exposed_ip4_port_on(self, network: ContainerNetwork) -> dict[str, dict]:
        return self.network.exposed_ip4_port()

    def url_domain(self) -> str:
        return self.config.url_domain()

    def url_path(self) -> str:
        return self.config.url_path()
