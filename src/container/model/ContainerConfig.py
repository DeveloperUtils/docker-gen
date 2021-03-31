import logging
from typing import Optional

from src.Config import KEY_ENABLED, KEY_OUTBOUND, KEY_URL, KEY_FORWARD_PORT, KEY_SSL_ENABLED, KEY_SSL_CERT_KEY, \
    KEY_SSL_CERT_CRT
from src.Utils import is_true

logger = logging.getLogger(__name__)


class ContainerConfig:
    raw: dict

    def __init__(self, labels: dict):
        self.raw = labels

    def is_enabled(self) -> bool:
        if KEY_ENABLED in self.raw.keys():
            return is_true(self.raw[KEY_ENABLED])
        else:
            return False

    def is_configured(self) -> bool:
        if KEY_URL in self.raw.keys():
            return True
        else:
            return False

    def is_public_gateway(self) -> bool:
        if KEY_OUTBOUND in self.raw.keys():
            return is_true(self.raw[KEY_OUTBOUND])
        else:
            return False

    def is_ssl_enabled(self) -> bool:
        if KEY_SSL_ENABLED in self.raw.keys():
            return is_true(self.raw[KEY_SSL_ENABLED])
        else:
            return True

    def ssl_cert_path_key(self) -> Optional[str]:
        if KEY_SSL_CERT_KEY in self.raw.keys():
            return str.strip(self.raw[KEY_SSL_CERT_KEY])

    def ssl_cert_path_crt(self) -> Optional[str]:
        if KEY_SSL_CERT_CRT in self.raw.keys():
            return str.strip(self.raw[KEY_SSL_CERT_CRT])

    def url_path(self) -> Optional[str]:
        if KEY_URL in self.raw.keys():
            split_: list[str] = self.raw[KEY_URL].split("/", 1)

            if len(split_) > 1 and len(str.strip(split_[1])) > 1:
                return split_[1]
        return "/"

    def url_domain(self) -> Optional[str]:
        logger.info("LABELS: %s", self.raw)
        if KEY_URL in self.raw.keys():
            split_ = self.raw[KEY_URL].split("/", 1)
            return split_[0]

    def get_forward_port(self) -> Optional[str]:
        if KEY_FORWARD_PORT in self.raw.keys():
            return str.strip(self.raw[KEY_FORWARD_PORT])
