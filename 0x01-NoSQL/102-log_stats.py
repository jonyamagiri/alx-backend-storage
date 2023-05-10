#!/usr/bin/env python3
""" module 102-log_stats.py """


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

total = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
methods_counts = [collection.count_documents({"method": method}) for method in methods]

path_count = collection.count_documents({"method": "GET", "path": "/status"})

ip_counts = collection.aggregate([
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

print(f"{total} logs")
print("Methods:")
for method, count in zip(methods, methods_counts):
    print(f"\tmethod {method}: {count}")
print(f"{path_count} status check")
print("IPs:")
for ip in ip_counts:
    print(f"\t{ip['_id']}: {ip['count']}")
