from unittest import TestCase

from house_screener.db.database_wrapper import DatabaseWrapper


class TestDatabaseWrapper(TestCase):
    dbWrapper: DatabaseWrapper

    def setUp(self):
        self.dbWrapper = DatabaseWrapper("testDb.db")

    def test_execute(self):
        self.dbWrapper.execute("CREATE TABLE testResult (testName TEXT, date DATE, result INIEGER)")