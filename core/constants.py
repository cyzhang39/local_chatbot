import os
from pathlib import Path

BASE_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '..'))
DEFAULT_ENV_FILE = os.path.abspath(os.path.join(BASE_DIR, "./configs/.env"))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def make_dirs(*dirs):
    for _dir in dirs:
        os.makedirs(_dir, exist_ok=True)

MODEL_URL = "http://127.0.0.1:8000"


