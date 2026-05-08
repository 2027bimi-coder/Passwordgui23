import sqlite3
from errno import EUSERS

from datetime import datetime

def checkAge(birthdate, minimumAge=13):
    try:
        # convert string from calendar into a date object
        birthDate = datetime.strptime(birthdate, "%m/%d/%Y")

        # today's date
        today = datetime.today()

        # basic age calculation
        age = today.year - birthDate.year

        # if birthday hasn't happened yet this year
        if (today.month, today.day) < (birthDate.month, birthDate.day):
            age -= 1

        return age >= minimumAge

    except ValueError:
        # invalid date format
        return False

def createUserTable():
    #create/access database file
    con = sqlite3.connect("user.db")
    #we need this to do anything in our database
    cur = con.cursor()


    #cur.execute("DROP TABLE users") # create a new table
    cur.execute("CREATE TABLE IF NOT EXISTS users(name, email, password, birthdate)") # create a new table

    con.commit()
    con.close()

#open/create database with file
def createRoleTable():

    con = sqlite3.connect("user.db")  # create/access database file
    cur = con.cursor()  # we need this to do anything in our database
    cur.execute("CREATE TABLE IF NOT EXISTS roles(userEmail, userRole, userView, userUpdate , userDelete)") # create a new table

    con.commit()
    con.close()

#recieve email from database
#If email match with whats written --> true
#if not return false
def lookupUser(email):
    con = sqlite3.connect("user.db")
    cur = con.cursor()

    results = cur.execute("SELECT email FROM users")

    for CurRow in results.fetchall():
        if email == CurRow[0]:
            con.close()
            return True

    con.close()
    return False

#print(lookupUser("2027bimi@seisen.com"))
def createUser(name, email, password, birthdate = None):
    if lookupUser(email) == False:
        con = sqlite3.connect("user.db")  # create/access database file

        cur = con.cursor()  # we need this to do anything in our database

        cur.execute("INSERT INTO users VALUES(?,?,?,?)", (name, email, password, birthdate))
        cur.execute("INSERT INTO roles VALUES(?,?,?,?,?)", (email, "user", False, False, False))# create a new table

        con.commit()
        con.close()
    else:
        print("User already exists.")

     #only creates user when they didnt exist)

#createUserTable()
#createUser ("Mirai", "2027bimi@seisen.com", "miraipassword", "0616")
#createRoleTable()

#login function --> check for matching username + password combo
def loginAttempt(email, password,):

    #If we dont --> return False
    con = sqlite3.connect("user.db")  # create/access database file
    cur = con.cursor()  # we need this to do anything in our database

    # find user with this email address
    results = cur.execute("SELECT email, password FROM users")  # create a new table
    #loop through all users
    for CurRow in results.fetchall():
            # if we find a matching email --> check if password matches
            if password == CurRow[1]:
                print("Logged in successfully.")
                con.close()
                return True
            # yes --> return true
            print(CurRow)
            con.close()
            return False

    con.close()
    return False

#If login is successful:
# finds the user's role from the roles table
#returns the role (admin, user, employee)
# If login fails:
# returns None
def lookUpRole(username, password):
    con = sqlite3.connect("user.db")
    cur = con.cursor()

    results = cur.execute("""SELECT users.email, roles.userRole, users.name
    FROM users
    JOIN roles
    ON users.email = roles.userEmail
    WHERE users.email=? AND users.password=?
    """, (username, password))

    row = results.fetchone()
    con.close()

    if row:
        # returns the role
        return row[1]
    return None


# check if the new role is valid, and if the user exists in the database
# if pass, updates the user's role, saves the changes to the database
def updateRole(userEmail, newRole):

    # allowed roles
    validRoles = ["admin", "user", "employee"]

    # check if role is valid
    if newRole not in validRoles:
        print("Invalid role.")
        return False

    con = sqlite3.connect("user.db")
    cur = con.cursor()

    # check if user exists
    cur.execute(
        "SELECT userEmail FROM roles WHERE userEmail=?",
        (userEmail,)
    )

    result = cur.fetchone()

    # if user does not exist
    if result is None:
        print("User not found.")
        con.close()
        return False

    # update role
    cur.execute(
        "UPDATE roles SET userRole=? WHERE userEmail=?",
        (newRole, userEmail)
    )

    con.commit()
    con.close()

    print("Role updated successfully.")
    return True



lookUpRole("2027bimi@seisen.com", "miraipassword")
