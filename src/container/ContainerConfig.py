from src.Utils import is_true

KEY_PREFIX = "com.github.developerutils.docker-gen"
KEY_ENABLED = KEY_PREFIX + ".enabled"


class ContainerConfig:
    raw: dict

    def __init__(self, labels: dict):
        self.raw = labels

    def is_enabled(self):
        return self.raw.keys().__contains__(KEY_ENABLED) \
               and is_true(self.raw[KEY_ENABLED])
