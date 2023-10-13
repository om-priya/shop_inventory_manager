"""
Context Manager for the db which automatically close the connection and handle the exception
"""
import sqlite3


class DatabaseConnection:
    """Context Manager Class for sqlite3"""

    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


"""
class SingletonDatabse:
    __instance = None

    @staticmethod
    def get_instance(host):
        if SingletonDatabse.__instance == None:
            SingletonDatabse(host)
        return SingletonDatabse.__instance

    def __init__(self, host):
        if SingletonDatabse.__instance != None:
            raise Exception("Don't create the object create using get_instance()")
        else:
            SingletonDatabse.__instance = self
            self.connection = None
            self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
"""
