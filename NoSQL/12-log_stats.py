#!/usr/bin/env python3
""" provides stats about nginx logs in mongodb """
import pymongo


def log_stats():
    """ provides some nginx stats """
    client = pymongo.MongoClient()
    db = client.logs
    logs = db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    status = logs.count_documents({'method': 'GET', 'path': '/status'})
    # print the number of logs
    print(f"{logs.count_documents({})} logs")
    # print the number of methods
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    # print status check
    print(f"{status} status check")

if __name__ == "__main__":
    log_stats()
