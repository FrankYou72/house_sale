from django.db import connection


def execute_query(query, params=None):
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [dict(zip(columns, item)) for item in rows]
        return rows
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    rows = [dict(zip(columns, item)) for item in rows]
    return rows
