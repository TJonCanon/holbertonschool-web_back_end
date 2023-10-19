#!/usr/bin/env python3
""" lists all docs in a collection """


import pymongo


def list_all(mongo_collection):
    """ lists docs in mongo_collection """
    return list(mongo_collection.find()) if mongo_collection is not None else []