
import SignUp
import LogIn
import Model
import smtplib
import sqlite3
from email.message import EmailMessage


#send an email to assigned email adress to reset password
def passwordResetEmail(*args):
    # get args for email and label
    print(args)
    email = args[1]
    errorLabel = args[2]


    # Email Content
    msg = EmailMessage()
    msg.set_content("Your password has been automatically reset to: TestPW1!. " +
                    "Please login and update your password.")
    msg['Subject'] = 'Password Reset Request'
    msg['From'] = "miraibistriteanucoco@gmail.com"
    msg['To'] = email

    # Send Email
    try:
        # Use App Password here, not your regular password
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("miraibistriteanucoco@gmail.com", "ammt vwwz ignz bivz")
        server.send_message(msg)
        server.quit()
        con = sqlite3.connect("user.db")
        cur = con.cursor()
        cur.execute("UPDATE users SET password=? WHERE email=?", ("TestPW1!", email))
        con.commit()
        con.close()

        errorLabel.config(text="Reset email sent!", fg="green")
    except Exception as e:
        print(e)
        errorLabel.config(text="Email not found or send failed", fg="red")

#code to create the windows
window, headFrame, signFrame, logInFrame = SignUp.setupWindow()

def backToLogin(event= None):
    SignUp.hideSignUp(signFrame, headFrame)
    LogIn.displayLogUp(logInFrame, headFrame)

def validatePW(*args):
    # args 0,1, and 2 are from the event
    # then password is 3, confirmPassword (4)
    # then labels list (5) [match, length, char]
    validPW = True
    password = args[3].get()
    confirmPassword = args[4].get()
    labels = args[5]

    print("called with:" + password)

    # check for special character
    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '?']
    foundchar = False

    for spchar in specialcharacters:
        if spchar in password:
            foundchar = True

    if len(password) < 8:
        validPW = False
        length = False
        SignUp.colorInvalidLabel(args[5][1])
    else:
        length = True
        SignUp.colorValidLabel(args[5][1])

    if not foundchar:
        validPW = False
        foundchar = False
        SignUp.colorInvalidLabel(args[5][2])
    else:
        foundchar = True
        SignUp.colorValidLabel(args[5][2])

    # check if passwords match
    if password != confirmPassword:
        SignUp.colorInvalidLabel(labels[0])
        validPW = False
    else:
        SignUp.colorValidLabel(labels[0])


    return validPW

#Call database
# updates error label with success/failure
def loginAttempt(email, password, errorLabel):
    print("called with " + email + " and " + password)

    if Model.loginAttempt(email, password):
        errorLabel.config(text="Login successful", fg="green")
    else:
        errorLabel.config(text="Invalid email or password", fg="red")


def submitAttempt(name, email, password, errorLabel, birthdate=None):
    print("called with:" + email + " and " + password)
# check if user already exists
    if Model.lookupUser(email):
        errorLabel.config(text="User already exists", fg="red")
        return

    # check password rules (SIMPLE VERSION)
    if len(password) < 8:
        errorLabel.config(text="Password must be at least 8 characters", fg="red")
        return

    if not any(char in "!@#$%^&*" for char in password):
        errorLabel.config(text="Password must include a special character", fg="red")
        return

    # create user
    if not Model.checkAge(birthdate):
        errorLabel.config(text="You must be at least 13 years old", fg="red")
        return
    Model.createUser(name, email, password, birthdate)

    # success message
    errorLabel.config(text="Account created!", fg="green")

    # go back to login page
    backToLogin(None)

    #if not eligibe for age, cannot create an account

    #are they 13 or over? 

def signUpPage(event):
    LogIn.hideLogIn(logInFrame, headFrame, passwordResetEmail)
    SignUp.displaySignUp(signFrame, headFrame, backToLogin)



SignUp.setUpSignUp(signFrame, headFrame, validatePW, submitAttempt, backToLogin)
logInFrame = LogIn.setUpLogIn(logInFrame, signUpPage, loginAttempt, passwordResetEmail)
#Display log in
LogIn.displayLogUp(logInFrame, headFrame)

#SignUp.displaySignUp(mainFrame, headFrame)

#SignUp.setUpSignUp(signFrame, headFrame)
#SignUp.hideSignUp(signFrame, headFrame)





window.mainloop() #update window


