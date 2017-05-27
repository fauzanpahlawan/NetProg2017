import sqlite3
from sqlite3 import Error
import json
import time


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def convert_data_to_json(rows):
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


def insert_into_employee(conn, data):
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES(?,?,?,?)"
    cur.execute(sql, data)


def select_all_employee(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM employee"
    cur.execute(sql)

    rows = cur.fetchall()
    return convert_data_to_json(rows)


def select_id_employee(conn, _id):
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE ID = (?)"
    cur.execute(sql, [_id])

    rows = cur.fetchall()
    return convert_data_to_json(rows)


def alter_from_employee(conn, data):
    cur = conn.cursor()
    sql = "UPDATE employee SET name = ?, position = ?, address = ? WHERE ID = ?"
    cur.execute(sql, data)


def delete_from_employee(conn, _id):
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE ID = (?)"
    cur.execute(sql, [_id])


def main():
    database = "employee.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # CREATE
        print("Original Data")
        print select_all_employee(conn) + "\n\n"

        time.sleep(1)
        print("Insert into table employee")
        insert_into_employee(conn, (4, "Miyamizu Mitsuha",
                                    "Head Research", "Toronto, Canada"))

        time.sleep(1)
        # READ
        print("Query select all from eployee.")
        print select_all_employee(conn) + "\n\n"
        print("Query select all from employee with id equal to 1")
        print select_id_employee(conn, 1) + "\n\n"

        time.sleep(1)
        # UPDATE
        print("Query update table employee with id equal to 4")
        alter_from_employee(
            conn, ("Miyamizu Mitsuha", "Head Research", "Toronto, Canada", 4))
        print select_id_employee(conn, 4) + "\n\n"

        time.sleep(1)
        # DELETE
        print("Delete from employee")
        delete_from_employee(conn, 4)

        time.sleep(1)
        print("Data after delete")
        print select_all_employee(conn) + "\n\n"


if __name__ == '__main__':
    main()
