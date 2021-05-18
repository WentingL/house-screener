class PreparedStatementBuffer:
    __str_list: list = []

    def __init__(self, table):
        self.table = table
        self.__str_list = []

    def select(self, *args):
        self.__str_list.append("SELECT ")
        self.__append_fields(*args)
        self.__str_list.append(" ")
        return self

    def update(self, fields, values):
        self.__str_list.append("UPDATE {} SET (".format(self.table))
        self.__append_fields(fields)
        self.__str_list.append(") VALUES (")
        self.__append_fields(values)
        self.__str_list.append(") ")
        return self

    def delete(self, condition):
        self.__str_list.append("DELETE FROM {} WHERE {} ".format(self.table, condition))
        return self

    def insert(self, fields, values):
        self.__str_list.append("INSERT INTO {} (".format(self.table))
        self.__append_fields(fields)
        self.__str_list.append(") VALUES (")
        self.__append_fields(values)
        self.__str_list.append(") ")
        return self

    def where(self, condition):
        """the condition should be in the format of 'field = value' or 'field like \'value\'"""
        self.__str_list.append("WHERE ")
        self.__str_list.append(condition)
        self.__str_list.append(" ")
        return self

    def __append_fields(self, fields):
        self.__str_list.append(', '.join(fields))

    def build(self) -> str:
        return ''.join(self.__str_list)


if __name__ == '__main__':
    stmt = PreparedStatementBuffer("testTable")
    stmt.select(('testField', 'testTestField'))
    stmt.where('name like \'OKTA\'')
    print(stmt.build())
