"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from sys import argv

import dotenv

dotenv.load_dotenv()

PORT: str = argv[3]
API_URL: str = f"localhost:{PORT}"
API_TOKEN: str = argv[2]
