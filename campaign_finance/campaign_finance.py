import schedule
import time

from extract import *
from transform import *
from load import *

def job():
    extract()
    transform()
    load()

schedule.every().saturday.at('19:03').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
