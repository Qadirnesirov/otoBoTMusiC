from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Mongo Databazanıza qoşulur...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Music
    LOGGER(__name__).info("Mongo verilənlər bazanıza qoşulub.")
except:
    LOGGER(__name__).error("Mongo Databazanıza qoşulmaq alınmadı.")
    exit()
  
