import sqlite3

def createUserTable():

    con = sqlite3.connect("user.db")  # create/access database file

    cur = con.cursor()  # we need this to do anything in our database


    #cur.execute("DROP TABLE users") # create a new table
    cur.execute("CREATE TABLE users(name, email, password, birthdate)") # create a new table

    con.commit() # save changes
    con.close() # end connection

def createRoleTable():

    con = sqlite3.connect("user.db")  # create/access database file

    cur = con.cursor()  # we need this to do anything in our database


    cur.execute("CREATE TABLE roles(userEmail, userRole, userVew, userUpdate , userDelete)") # create a new table

    con.commit() # save changes
    con.close() # end connection

def lookupUser(email):
    con = sqlite3.connect("user.db")  # create/access database file

    cur = con.cursor()  # we need this to do anything in our database

    results = cur.execute("SELECT email FROM users")  # create a new table
    for CurRow in results.fetchall():
        if email in CurRow:
            con.close()  # end connection
            return True

    con.close()  # end connection
    return False

#print(lookupUser("2027bimi@seisen.com"))
def createUser(name, email, password, birthdate = None):
    if lookupUser(email) == False:
        con = sqlite3.connect("user.db")  # create/access database file

        cur = con.cursor()  # we need this to do anything in our database

        cur.execute("INSERT INTO users VALUES(?,?,?,?)", (name, email, password, birthdate))
        cur.execute("INSERT INTO users VALUES(?,?,?,?)", (name, email, password, birthdate))# create a new table

        con.commit()  # save changes
        con.close()  # end connection
    else:
        print("User already exists.")

     #only creates user when they didnt exist)

#createUserTable()
#createUser ("Mirai", "2027bimi@seisen.com", "miraipassword", "0616")
#createRoleTable()
