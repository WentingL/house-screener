import unittest

from house_screener.db.prepared_statement import PreparedStatementBuffer


class TestPreparedStatementBuffer(unittest.TestCase):
    testStmt: PreparedStatementBuffer
    table = "test_table"

    def setUp(self) -> None:
        self.testStmt = PreparedStatementBuffer(self.table)

    def tearDown(self) -> None:
        self.testStmt: PreparedStatementBuffer

    def test_select(self):
        fields = ["test_field1", "test_field2", "test_field3", ]
        self.assertEqual("SELECT {}, {}, {} ".format(fields[0], fields[1], fields[2]),
                         self.testStmt.select(fields).build())

    def test_update(self):
        fields = ["test_field1", "test_field2", "test_field3", ]
        values = ["test_value1", "test_value2", "test_value3", ]
        self.assertEqual(
            "UPDATE {} SET ({}, {}, {}) VALUES ({}, {}, {}) ".format(self.table, fields[0], fields[1], fields[2],
                                                                     values[0], values[1], values[2]),
            self.testStmt.update(fields, values).build())

    def test_delete(self):
        self.assertEqual("DELETE FROM test_table WHERE test = condition ",
                         self.testStmt.delete("test = condition").build())

    def test_insert(self):
        fields = ["test_field1", "test_field2", "test_field3", ]
        values = ["test_value1", "test_value2", "test_value3", ]
        self.assertEqual(
            "INSERT INTO {} ({}, {}, {}) VALUES ({}, {}, {}) ".format(self.table, fields[0], fields[1], fields[2],
                                                                      values[0], values[1], values[2]),
            self.testStmt.insert(fields, values).build())

    def test_where(self):
        self.assertEqual("WHERE test = condition ", self.testStmt.where("test = condition").build())


if __name__ == '__main__':
    unittest.main()
