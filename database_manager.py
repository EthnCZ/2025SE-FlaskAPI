from flask import jsonify
import sqlite3 as sql
from jsonschema import validate
from flask import current_app


def extension_get():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM extension")
    migrate_data = [
        dict(
            extID=row[0],
            name=row[1],
            hyperlink=row[2],
            about=row[3],
            image=row[4],
            language=row[5],
        )
        for row in cur.fetchall()
    ]
    return jsonify(migrate_data)