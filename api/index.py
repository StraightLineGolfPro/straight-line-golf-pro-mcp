"""Isolated Vercel ASGI entry point."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from remote import create_app
app = create_app()
