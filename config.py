import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret-key")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(INSTANCE_DIR, 'expenses.db')}",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False