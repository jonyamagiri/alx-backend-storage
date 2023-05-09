#!/usr/bin/env python3
""" module 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools that have a specific topic.
    Args:
        mongo_collection: The MongoDB collection to search.
        topic (str): The topic to search for.
    Returns:
        A generator expression that yields each matching document.
    """
    filter_topic = {'topics': {'$elemMatch': {'$eq': topic}}}
    return mongo_collection.find(filter_topic)
