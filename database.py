# Contains DB Connection and Schema, and insertion logic
import sqlite3 



# ✅ 3. Save to SQLite .db

def createConnection():
    conn = sqlite3.connect("parsed_logs.db")
    return conn.cursor(),conn

def createTable(self,cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            ip TEXT,
            timestamp TEXT,
            method TEXT,
            url TEXT,
            protocol TEXT,
            status INTEGER,
            size TEXT
        )
        """)
    
def insertData(self,conn,cur,parsed_logs):
    # Insert data
    for log in parsed_logs:
        cur.execute("""
        INSERT INTO logs (ip, timestamp, method, url, protocol, status, size)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            log["ip"], log["timestamp"], log["method"], log["url"],
            log["protocol"], int(log["status"]), log["size"]
        ))

    conn.commit()
    conn.close()