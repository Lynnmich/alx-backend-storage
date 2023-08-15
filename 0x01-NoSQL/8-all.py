#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""


def list_all(mongo_collection)
    """Returns an empty list if no doc is in the collection"""
    return mongo_collection.find()
