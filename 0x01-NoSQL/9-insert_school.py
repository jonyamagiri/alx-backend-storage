#!/usr/bin/env python3
""" module 9-insert_school.py """


def insert_school(mongo_collection, **kwargs) -> str:
    """
    Inserts a new document into a collection.
    Args:
        mongo_collection: PyMongo collection object.
        kwargs: dictionary containing fields and values for the new document.
    Returns:
        str: The ID of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
