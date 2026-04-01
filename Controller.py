
import SignUp
import LogIn

#code to create the windows
window, headFrame, logInFrame, signFrame = SignUp.setupWindow()


def validatePW(*args):
    # args 0,1, and 2 are from the event
    # then password is 3, confirmPassword (4)
    # then labels list (5) [match, length, char]
    validPW = True
    password = args[3].get()
    print("called with:" + password)

    # check for special character
    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '?']
    foundchar = False

    for spchar in specialcharacters:
        if spchar in password:
            foundchar = True

    if len(password) < 8:
        length = False
        SignUp.colorInvalidLabel(args[5][1])
    else:
        length = True
        SignUp.colorValidLabel(args[5][1])

    if not foundchar:
        foundchar = False
        SignUp.colorInvalidLabel(args[5][2])
    else:
        foundchar = True
        SignUp.colorValidLabel(args[5][2])


    return validPW


def loginAttempt(email,password, errorLabel):
    print ("called with " + email +"and" + password)





def signUpPage(event):
    LogIn.hideLogIn(logInFrame, headFrame)
    SignUp.displaySignUp(signFrame, headFrame)


SignUp.setUpSignUp(signFrame, headFrame, validatePW)
logInFrame = LogIn.setUpLogIn(logInFrame, signUpPage, loginAttempt)
#Display log in
LogIn.displayLogUp(logInFrame, headFrame)

#SignUp.displaySignUp(mainFrame, headFrame)

#SignUp.setUpSignUp(signFrame, headFrame)
#SignUp.hideSignUp(signFrame, headFrame)





window.mainloop() #update window


