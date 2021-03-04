from docker.models.containers import Container

from src.container.ContainerConfig import ContainerConfig


class ContainerWrapper:

    def __init__(self, container_info: Container):
        self.raw: dict = container_info.attrs
        self.wrapped: Container = container_info
        self.config: ContainerConfig = ContainerConfig(self.wrapped.labels)

    def is_running(self) -> bool:
        return self.wrapped.status == 'running'

    def id(self) -> str:
        return self.wrapped.id

    def networks(self) -> dict:
        return {}

    def is_relevant(self) -> bool:
        return self.config.is_enabled()
