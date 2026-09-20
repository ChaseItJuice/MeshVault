"""
MeshVault Configuration & Environment Variables Management
Loads configuration from .env file and environment variables.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend directory or project root
backend_dir = Path(__file__).resolve().parent
root_dir = backend_dir.parent

load_dotenv(backend_dir / ".env")
load_dotenv(root_dir / ".env")

# ─── Environment Variables ────────────────────────────────────────────────────

DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./meshvault.db")
SECRET_KEY: str = os.getenv("SECRET_KEY", "meshvault-dev-secret-key-replace-in-production-f9b3e1")
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
ALLOWED_ORIGINS: list[str] = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "").split(",")
    if origin.strip()
]

# ─── Normalize Connection String ──────────────────────────────────────────────

# Render/Heroku inject postgres://, which SQLAlchemy psycopg2 requires as postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


