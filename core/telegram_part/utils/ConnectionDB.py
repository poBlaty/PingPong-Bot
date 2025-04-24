from redis.asyncio import ConnectionPool, Redis
import redis

from core.telegram_part.utils.settings import Settings


class ConnectionDB:

    def __create_connection_pool(self) -> ConnectionPool:
        try:
            connection_pool = ConnectionPool(host=self.__ip, port=self.__port, password=self.__password,
                                             decode_responses=True, max_connections=3)
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            raise ConnectionRefusedError

        return connection_pool

    def __init__(self, settings: Settings):
        self.__ip = settings.redis.ip
        self.__port = settings.redis.port
        self.__password = settings.redis.password
        self.__connection_pool: ConnectionPool = self.__create_connection_pool()

    async def get_connection(self) -> Redis:
        return Redis(connection_pool=self.__connection_pool)

    def get_pool(self) -> ConnectionPool:
        return self.__connection_pool

    async def close(self):
        await self.__connection_pool.aclose()