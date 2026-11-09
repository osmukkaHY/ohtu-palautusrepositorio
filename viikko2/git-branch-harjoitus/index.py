# imports

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: "))  # other
y = int(input("luku 2: "))  # other
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
logger("hei hei")
