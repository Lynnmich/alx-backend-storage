#!/usr/bin/env python3
"""Python function that changes all topics of a school doc based on name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school doc"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
