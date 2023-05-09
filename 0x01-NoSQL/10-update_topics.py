#!/usr/bin/env python3
""" module 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """Update the topics for a document in the given collection.
    Args:
        mongo_collection: The MongoDB collection to update.
        name (str): The name of the document to update.
        topics (list): The list of new topics to set for the document.
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)
