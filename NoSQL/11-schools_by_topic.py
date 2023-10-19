#!/usr/bin/env python3
""" returns list of schools that have a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools with topic """
    return mongo_collection.find(
        {"topics": topic}
    ) if mongo_collection is not None else []