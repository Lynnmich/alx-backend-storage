i#!/usr/bin/env python3
"""A Python function that inserts a new doc in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    new_id = mongo_collection.insert_one(kwargs).new_id
    return new_id
