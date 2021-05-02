from pathlib import Path

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_VARIABLES = f"""SECRET_KEY={get_random_secret_key()}
DEBUG=True
"""

file = open(f"{BASE_DIR}/library/.env", "w")
file.write(ENV_VARIABLES)
