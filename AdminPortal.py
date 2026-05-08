import sqlite3

#User enters email + password
#Program connects to database
#Checks users table for matching login
#Connects matching user to roles table
#Finds the user's role
# Displays: Login successful, Role (admin/user/employee)

email = input("Email: ")
password = input("Password: ")

# connect to the database file
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
