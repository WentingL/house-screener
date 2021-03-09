import sqlite3
from house_screener.db.DatabaseError import DatabaseInteractionException

class DatabaseWrapper:
    db_source = "sourceDatabase.db"
    db_analysis = "analysisDatabase.db"

    def __init__(self):
        self.conn = None
        self.cursor = None

    def get_connection(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error or Exception:
            raise DatabaseInteractionException("Cannot establish database connection")

    def update(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def create_table(self):
        pass

    def read_with_id(self):
        pass

    def read_with_fields(self):
        pass


if __name__ == "__main__":
    db_wrapper = DatabaseWrapper()
    db_wrapper.get_connection(db_wrapper.db_analysis)
