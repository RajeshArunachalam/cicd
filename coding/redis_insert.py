import json
import redis
import csv
import itertools

freq = 0
dic_list = []
DX_CODE_COLUMN = "Text"
DISEASE_COLUMN_NAME = "Disease"

# Create a redis client
redisClient = redis.StrictRedis(
    host="localhost", port=6379, db=1, charset="utf-8", decode_responses=True
)

# Add dictionary key/value pairs to the Redis database
def insert(freq, csv_file_path):
    freq = freq + 1

    if freq == 0:
        with open(csv_file_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                redisClient.set(str(row[DX_CODE_COLUMN]), str(row[DISEASE_COLUMN_NAME]))
        return redisClient
    else:
        return redisClient


def get_matches(redisClient, pattern):
    print(redisClient)
    list_of_match = []
    count = 0
    for key in redisClient.keys():
        count += 1
        list_of_match.append(key + ":" + str(redisClient.get(key)))
        matching = [s for s in list_of_match if pattern in s]
        if len(list_of_match) > 0:
            dic_list.append(matching)
        list_of_match.clear()
    print("count", count)
    res = list(filter(None, dic_list))
    flat_list = [item for sublist in res for item in sublist]
    return flat_list
