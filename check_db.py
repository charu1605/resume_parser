import sqlite3

conn = sqlite3.connect("resume.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM resumes").fetchall()

print("Total records:", len(rows))
print("-" * 50)

for row in rows:
    print(row)

conn.close()
