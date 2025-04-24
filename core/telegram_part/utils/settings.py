from typing import NamedTuple
from dotenv import load_dotenv
import os


class Bots(NamedTuple):
    token: str
    admin_id: list[int | str]


class Redis(NamedTuple):
    ip: str
    port: str
    password: str


class Settings(NamedTuple):
    bots: Bots
    redis: Redis


def _get_settings(path: str):
    load_dotenv(dotenv_path=path)

    token = os.getenv("TOKEN")
    admin_id = os.getenv("ADMIN_ID").split(" ")

    ip = os.getenv("DB_IP")
    port = os.getenv("DB_PORT")
    password = os.getenv("DB_PASSWORD")

    return Settings(
        bots=Bots(
            token=token,
            admin_id=admin_id),
        redis=Redis(
            ip=ip,
            port=port,
            password=password)
    )


settings = _get_settings('.env')
