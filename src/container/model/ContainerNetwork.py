import logging

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


class NetworkSettings:
    """
        "NetworkSettings": {
        "Bridge": "",
        "SandboxID": "73c2f6f22e3e8e77c49dcf3f4d219070c6424b458df143d7b716a5d24a1f944a",
        "HairpinMode": False,
        "LinkLocalIPv6Address": "",
        "LinkLocalIPv6PrefixLen": 0,
        "Ports": {
            "8000/tcp": None,
            "9000/tcp": [
                {
                    "HostIp": "0.0.0.0",
                    "HostPort": "9000"
                }
            ]
        },
        "SandboxKey": "/var/run/docker/netns/73c2f6f22e3e",
        "SecondaryIPAddresses": None,
        "SecondaryIPv6Addresses": None,
        "EndpointID": "",
        "Gateway": "",
        "GlobalIPv6Address": "",
        "GlobalIPv6PrefixLen": 0,
        "IPAddress": "",
        "IPPrefixLen": 0,
        "IPv6Gateway": "",
        "MacAddress": "",
        "Networks": {
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
        }
    }
    """
    raw: dict

    def __init__(self, settings: dict):
        self.raw = settings
        self._networks: dict[ContainerNetwork] = self.get_all_networks(self.raw)
        self.ports: Ports = Ports(self.raw["Ports"])

    def exposed_ip4_address(self) -> str:
        first_network: ContainerNetwork = list(self._networks.values())[0]
        return first_network.get_ip4_address()

    def exposed_ip4_port(self) -> dict[str]:
        return self.ports.get_exposed()

    @staticmethod
    def get_all_networks(attrs: dict) -> dict[ContainerNetwork]:
        networks: dict = attrs["Networks"]
        ret: dict = {}
        for network_id, network in networks.items():
            ret[network_id] = ContainerNetwork(network_id, network)
        return ret


class Ports:
    """
    "Ports": {
        "8000/tcp": None,
        "9000/tcp": [
            {
                "HostIp": "0.0.0.0",
                "HostPort": "9000"
            }
        ]
    },
    """
    raw: dict

    def __init__(self, ports: dict):
        self.raw = ports

    def get_exposed(self) -> dict[str]:
        ret: dict[str] = {}
        for key in self.raw:
            if self.raw[key]:
                splits = key.split("/")
                ret[splits[1]] = splits[0]
        return ret
