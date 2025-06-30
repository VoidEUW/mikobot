"""MikoBot (c) 2024-2025 by Void"""

import os

import dotenv


dotenv.load_dotenv()

# Setup configuration
FIRST_SETUP: str = os.getenv("FIRST_SETUP", "False")
USERNAME: str = os.getenv("USERNAME", "admin")
PASSWORD: str = os.getenv("PASSWORD", "password123")
EMAIL: str = os.getenv("EMAIL", "admin@example.com")

# Server configuration
SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
DEBUG: bool = os.getenv("DEBUG", "false") == "true"
HOST: str = "0.0.0.0"
PORT: int = 8080

# Path configuration
PATH_DATABASE: str = "database/data/database.db"

# API configuration
API_URL: str = "http://localhost:8080"
API_TOKEN: str = os.getenv("API_TOKEN", "default_token")
API_VERSION: str = "v1"
API_SLUG: str = f"/api/{API_VERSION}"

# Bot configuration
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")