import sqlite3
from typing import List, Dict, Any

def get_db_connection():
    conn = sqlite3.connect("data/presidents.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_all_presidents() -> List[Dict[str, Any]]:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM presidents")
    rows = cursor.fetchall()
    
    presidents = []
    for row in rows:
        president = dict(row)
        cursor.execute("SELECT name FROM legislation WHERE president_id = ?", (president["id"],))
        legislation_rows = cursor.fetchall()
        president["legislation"] = [l["name"] for l in legislation_rows]
        presidents.append(president)
        
    conn.close()
    return presidents
