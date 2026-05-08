import sqlite3

email = input("Email: ")
password = input("Password: ")

conn = sqlite3.connect("user.db")
cur = conn.cursor()

sql = """
SELECT users.email, roles.UserRole
FROM users
JOIN roles
ON users.email = roles.userEmail
WHERE users.email=? AND users.password=?
"""

cur.execute(sql, (email, password))
result = cur.fetchone()

conn.close()

if result:
    print("Login successful!")
    print("Role:", result[1])
else:
    print("Login failed.")
