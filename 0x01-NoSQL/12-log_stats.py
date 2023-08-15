#!/usr/bin/env python3
""" Python script that provides stats about Nginx logs stored in MongoDB"""
import pymongo as pm
db = pm.MongoClient()
mydb = db["logs"]
mycoll = mydb["nginx"]


if __name__ == "__main__":
    get_get = mycoll.count_documents({"method": "GET"})
    get_post = mycoll.count_documents({"method": "POST"})
    get_put = mycoll.count_documents({"method": "PUT"})
    get_patch = mycoll.count_documents({"method": "PATCH"})
    get_delete = mycoll.count_documents({"method": "DELETE"})
    get_total = mycoll.count_documents({})
    get_status = mycoll.count_documents({"method": "GET", "path": "/status"})


    print("{} logs".format(get_total))
    print("Methods:\n\tmethod GET: {}\n\tmethod POST: {}\n\tmethod PUT: {}\n\tmethod PATCH: {}\n\tmethod DELETE: {}".format(
                  get_get, get_post, get_put, get_patch, get_delete))
    print("{} status check".format(get_status))
