import json
import sqlite3
from werkzeug.datastructures import ImmutableMultiDict

__all__ = ['save_driver_call', 'get_driver_calls']
DATABASE = 'db.sqlite'


def create_db():
    print("***********************************************")
    print("Create database...")
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('CREATE TABLE driver_calls (driver_id varchar(10), data json)')
    except Exception as exc:
        print(exc.__class__, ':', exc)


create_db()


def save_driver_call(data: ImmutableMultiDict):
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('INSERT INTO driver_calls values (?, ?)', (data['driver_id'], json.dumps(data)))
        con.commit()


def get_driver_calls(driver_id=None):
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        if driver_id:
            cur.execute('SELECT * FROM driver_calls')
        else:
            cur.execute('SELECT * FROM driver_calls WHERE driver_id=?', [driver_id])
        rows = cur.fetchall()
        return [json.loads(row[1]) for row in rows]
