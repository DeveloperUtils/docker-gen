import logging
from collections import Set

logger = logging.getLogger(__name__)


class ContainerNetwork:
    """
        "simple_portainer_default": {
            "IPAMConfig": None,
            "Links": None,
            "Aliases": [
                "672f2b5f8ad8",
                "portainer"
            ],
            "NetworkID": "e32599046e32d41c136756b2dd380196f86392792a3b04df09a855ff91467bfd",
            "EndpointID": "85b5d42e4b4732a7acbd9616a9d74bfbfd5c3b79c226d282d14cd35b02475edc",
            "Gateway": "172.22.0.1",
            "IPAddress": "172.22.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "MacAddress": "02:42:ac:16:00:02",
            "DriverOpts": None
        }
    """

    def __init__(self, name: str, raw: dict):
        self.name: str = name
        self.raw: dict = raw

    def id(self) -> str:
        return self.raw["NetworkID"]

    def name(self) -> str:
        return self.name

    def names(self) -> set[str]:
        ret = {self.name}
        for alias in self.raw["Aliases"]:
            ret.add(alias)
        return ret

    def get_ip4_address(self) -> str:
        return self.raw["IPAddress"]
