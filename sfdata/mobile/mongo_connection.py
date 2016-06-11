from pymongo import MongoClient

CONN_SETTINGS_READ  = {'host': 'localhost', 'port': 27000}


class QGMongo(object):
    __conn_read = None
    __conn_write = None

    @classmethod
    def get_connection(cls):
        if cls.__conn_read is None:
            cls.__conn_read = MongoClient(**CONN_SETTINGS_READ)
        return cls.__conn_read

