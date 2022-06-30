import os
from .redis_insert import insert, get_matches
import datetime
from curie.celery import app
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@app.task(bind=True)
def newprocess(self, freq, searchKey):
    fre = freq
    search_pattern = searchKey
    a = datetime.datetime.now()
    icd_10_db_csv = env("ICD10_FILE")
    redisClient = insert(fre, icd_10_db_csv)
    print(redisClient)
    matches = get_matches(redisClient, search_pattern)
    print(matches)
    b = datetime.datetime.now()
    print(b - a)
