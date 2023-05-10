#!/usr/bin/env python3
""" module 101-students.py """


def top_students(mongo_collection):
    """
    Returns all students in a collection sorted by average score.
    Args:
        mongo_collection: pymongo collection object
    Returns:
        pymongo aggregation object containing students sorted by average score
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'},
                'topics': 1
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    students = list(mongo_collection.aggregate(pipeline))
    return students
