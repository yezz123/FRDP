import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    pass


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn(
            "Could not disconnect from database. This is probably because the connection was never established."
        )
        logger.warn(e)
        logger.warn(
            "If you are running tests, this is probably because you are not using the test database."
        )
