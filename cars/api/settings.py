import os

DB_HOST = os.environ.get("DB_HOST", "0.0.0.0")
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ["DB_NAME"]

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
