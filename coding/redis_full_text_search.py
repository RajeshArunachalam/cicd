import datetime
from redis_insert import insert, get_matches

search_pattern = "cholera"
a = datetime.datetime.now()
icd_10_db_csv = "/home/waterlabs/Documents/curie/curie/ICD10-Data.csv"
redisClient = insert(icd_10_db_csv)
matches = get_matches(redisClient, search_pattern)
print(matches)
b = datetime.datetime.now()
print(b - a)
