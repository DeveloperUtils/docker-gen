#!/usr/bin/env python3

from src.App import App
from src.Utils import initialize_logger

initialize_logger("./logs")

if __name__ == '__main__':
    app = App()
    app.run()
