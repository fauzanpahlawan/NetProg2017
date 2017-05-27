import sqlite3
from sqlite3 import Error
import json

database = 'employee.db'


def create_connection():
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
        return None


def convert_rows_to_json(rows):
    list_data = []
    for row in rows:
        dict_employee = {
            "id": row[0],
            "name": row[1],
            "position": row[2],
            "address": row[3]
        }
        list_data.append(dict_employee)
    data_dict = {
        "num": len(rows),
        "data": list_data
    }
    return json.dumps(data_dict)


def select_all(table):
    conn = create_connection()
    cur = conn.cursor()
    query = "SELECT * FROM {}".format(table)
    cur.execute(query)
    rows = cur.fetchall()
    return convert_rows_to_json(rows)
    conn.close()


def select_one(table, _id):
    conn = create_connection()
    cur = conn.cursor()
    query = 'SELECT * FROM {} WHERE ID = ?'.format(table)
    cur.execute(query, (_id,))
    rows = cur.fetchall()
    return convert_rows_to_json(rows)
    conn.close()


def insert_into(table, data):
    try:
        conn = create_connection()
        cur = conn.cursor()
        query = 'INSERT INTO {} VALUES(?,?,?,?)'.format(table)
        cur.execute(query, data)
        conn.commit()
        conn.close()
        return json.dumps({"status": "Success"})
    except:
        return jsom.dumps({"status": "Failed"})


def alter_table(table, data):
    try:
        conn = create_connection()
        cur = conn.cursor()
        query = 'UPDATE {} SET name = ?, position = ?, address = ? WHERE ID = ?'.format(
            table)
        cur.execute(query, data)
        conn.commit()
        conn.close()
        return json.dumps({"status": "Success"})
    except:
        return json.dumps({"status": "Failed"})


def delete_from(table, _id):
    try:
        conn = create_connection()
        cur = conn.cursor()
        query = 'DELETE FROM {} WHERE ID = ?'.format(table)
        cur.execute(query, (_id,))
        conn.commit()
        conn.close()
        return json.dumps({"status": "Success"})
    except:
        return json.dumps({"status": "Failed"})