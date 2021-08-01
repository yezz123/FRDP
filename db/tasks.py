from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    pass


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ---")
