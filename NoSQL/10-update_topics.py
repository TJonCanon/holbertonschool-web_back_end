#!/usr/bin/env python3
""" changes all topics of a school doc based on the name """


import pymongo


def update_topics(mongo_collection, name, topics):
    """ changers all topics """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    ) if mongo_collection is not None else None
