import sqlite3

from house_screener.db.database_error import DatabaseInteractionException


class DatabaseWrapper:
    db_source = "sourceDatabase.db"
    db_analysis = "analysisDatabase.db"

    def __init__(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except Exception:
            raise DatabaseInteractionException("Cannot establish database connection")

    def execute(self, query):
        self.cursor.execute(query)


if __name__ == "__main__":
    db_wrapper = DatabaseWrapper()
    db_wrapper.get_connection(db_wrapper.db_analysis)
