import argparse

from src.App import App
from src.Utils import initialize_logger

initialize_logger("./logs")

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--daemon", help="start as daemon", action="store_true")
args = parser.parse_args()

app = App()

if args.daemon:
    app.run_as_daemon()
else:
    app.run_once()
