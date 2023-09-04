#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs
    collection = db.nginx

    totalLogs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methodCount = {method: collection.count_documents(
        {"method": method}) for method in methods}

    statusCheck = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{totalLogs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}:", methodCount[method])
    print(f"{statusCheck} status check")


if __name__ == "__main__":
    log_stats()
