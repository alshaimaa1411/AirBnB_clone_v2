#!/usr/bin/python3
"""db_storage"""
import MySQLdb
import sys

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = MySQLdb.Connect(host="HBNB_MYSQL_HOST", user="HBNB_MYSQL_USER",
                                        password="HBNB_MYSQL_PWD", dbname="HBNB_MYSQL_DB")