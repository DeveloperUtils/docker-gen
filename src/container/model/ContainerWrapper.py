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
        return self.wrapped.name

    def is_relevant(self) -> bool:
        return self.config.is_enabled()
