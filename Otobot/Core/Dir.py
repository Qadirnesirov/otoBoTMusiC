import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "endirmələr" not in os.listdir():
        os.mkdir("endirmələr")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Kataloqlar Yenilənib.")
  
