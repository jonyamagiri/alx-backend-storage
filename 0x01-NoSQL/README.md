# 0x01. NoSQL

> This repository contains the tasks for `NoSQL` project and a description of what each program or function does:


## Learning Objectives

	* What NoSQL means
	* What is difference between SQL and NoSQL
	* What is ACID
	* What is a document storage
	* What are NoSQL types
	* What are benefits of a NoSQL database
	* How to query information from a NoSQL database
	* How to insert/update/delete information from a NoSQL database
	* How to use MongoDB


* NoSQL (Not only SQL) is a type of database management system that differs from traditional relational databases in that it does not use a fixed schema for organizing data. Instead, NoSQL databases are designed to handle unstructured and semi-structured data, making them suitable for big data applications where data structures can be highly variable.

* Here are some examples of NoSQL database management systems (DBMS):
- [x] MongoDB: This is a popular document-oriented NoSQL database that stores data in JSON-like documents.
- [x] Cassandra: This is a distributed NoSQL database that can handle large amounts of data across multiple commodity servers.
- [x] Couchbase: This is a NoSQL database that supports both document-oriented and key-value data models.
- [x] Redis: This is an in-memory NoSQL database that supports key-value data model.
- [x] Amazon DynamoDB: This is a fully managed NoSQL database service that provides features like scalability, high performance, and automatic scaling.

* Here are some general steps for using MongoDB:
- [x] Start MongoDB: For example, on Linux, you might run the command `sudo service mongod start`.
- [x] Create a database: For example, to create a database named "mydb", you would run the command `use mydb`.
- [x] Create a collection: For example, to create a collection named "users", you would run the command `db.createCollection("users")`.
- [x] Insert data: To insert data into a collection, you can use the `db.collection.insertOne()` or `db.collection.insertMany()` commands.
- [x] Query data: For example, to retrieve all users from the "users" collection, you might run the command: `db.users.find()`


## Tasks

- [x] Task: 0-list_databases
- [x] Task: 1-use_or_create_database
- [x] Task: 2-insert
- [x] Task: 3-all
- [x] Task: 4-match
- [x] Task: 5-count
- [x] Task: 6-update
- [x] Task: 7-delete
- [x] Task: 8-all.py
- [x] Task: 9-insert_school.py
- [x] Task: 10-update_topics.py
- [x] Task: 11-schools_by_topic.py
- [x] Task: 12-log_stats.py
- [x] Task: 100-find
- [x] Task: 101-students.py
- [x] Task: 102-log_stats.py

___


