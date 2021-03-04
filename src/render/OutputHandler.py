# -*- coding: utf-8 -*-

import logging
import os

from jinja2 import Environment

logger = logging.getLogger(__name__)


class OutputHandler:

    def __init__(self, j2_env: Environment, template_dir: str, output_dir: str):
        self.j2_env = j2_env
        self.template_dir = template_dir
        self.output_dir = output_dir

    def run(self, j2_context: dict):
        logger.info("Template Dir: %s, Output Dir: %s", self.template_dir, self.output_dir)
        with os.scandir(self.template_dir) as dirs:
            for entry in dirs:
                if entry.name.endswith(".j2"):
                    render = self.j2_env.get_template(entry.name).render(j2_context)
                    with open(os.path.join(self.output_dir, os.path.splitext(entry.name)[0]), 'w') as out_file:
                        out_file.write(render)
                    logger.info("Ren: %s", render)
                logger.info("Rendering %s", entry.name)
