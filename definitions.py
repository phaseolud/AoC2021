import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent
DAY_DIR = ROOT_DIR / "days"
HELPER_DIR = ROOT_DIR / "helpers"
SESSION = os.getenv("SESSION")
