class PreparedStatementBuffer:
    __str_list: list = []

    def __init__(self, table):
        self.table = table

    def select(self, *args):
        self.__str_list.append("SELECT ")
        self.__append_fields(*args)
        self.__str_list.append(" ")

    def update(self, fields, values):
        self.__str_list.append("UPDATE {} SET (".format(self.table))
        self.__append_fields(fields)
        self.__str_list.append(") VALUES (")
        self.__append_fields(values)
        self.__str_list.append(") ")

    def delete(self, condition):
        self.__str_list.append("DELETE FROM {} WHERE {} ".format(self.table, condition))

    def insert(self, fields, values):
        self.__str_list.append("INSERT INTO {} (".format(self.table))
        self.__append_fields(fields)
        self.__str_list.append(") VALUES (")
        self.__append_fields(values)
        self.__str_list.append(") ")

    def where(self, condition):
        """the condition should be in the format of 'field = value' or 'field like \'value\'"""
        self.__str_list.append("WHERE ")
        self.__str_list.append(condition)
        self.__str_list.append(" ")

    def __append_fields(self, fields):
        for f in fields:
            self.__str_list.append(f)
            self.__str_list.append(", ")
        self.__str_list.pop(-1)

    def build(self) -> str:
        return ''.join(self.__str_list)


if __name__ == '__main__':
    stmt = PreparedStatementBuffer("testTable")
    stmt.select(('testField', 'testTestField'))
    stmt.where('name like \'OKTA\'')
    print(stmt.build())
