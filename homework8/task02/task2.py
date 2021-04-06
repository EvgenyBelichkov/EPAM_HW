"""
Write a wrapper class TableData for database table, that when initialized with database name and table
acts as collection object (implements Collection protocol). Assume all data has unique values in 'name'
column. So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
    1) len(presidents) will give current amount of rows in presidents table in database
    2) presidents['Yeltsin'] should return single data row for president with name Yeltsin
    3) 'Yeltsin' in presidents should return if president with same name exists in table
    4) object implements iteration protocol. i.e. you could use it in for loops::
        for president in presidents:
            print(president['name'])
    5) all above mentioned calls should reflect most recent data. If data in table changed
       after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the
first record, then go to the next one, until records are exhausted. When writing tests,
it's not always neccessary to mock database calls completely. Use supplied example.sqlite file
as database fixture file.
"""

import sqlite3


class TableData:
    def __init__(self, database_name="example.sqlite", table_name="presidents"):
        self.database_name = database_name
        self.table_name = table_name

    def __len__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        sql_request = f"SELECT COUNT(*) from {self.table_name}"
        cursor.execute(sql_request)
        return cursor.fetchone()[0]

    def __getitem__(self, requested_name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        sql_request = (
            f"SELECT * from {self.table_name} where name=:name ",
            {"name": requested_name},
        )
        cursor.execute(*sql_request)
        return cursor.fetchone()

    def __contains__(self, item):
        return self[item]

    def __iter__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        yield from cursor.execute(f"SELECT * from {self.table_name}")
