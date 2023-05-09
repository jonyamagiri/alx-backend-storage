#!/usr/bin/env python3
""" module 8-all.py """

import pymongo


def list_all(mongo_collection) -> list:
    """
    Lists all documents in a collection.
    Args:
        mongo_collection: A PyMongo collection object.
    Returns:
        list: A list of all documents in the collection.
    """
    cursor = mongo_collection.find()
    documents = [doc for doc in cursor]
    return documents
