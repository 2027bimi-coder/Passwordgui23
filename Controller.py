
import SignUp
import LogIn
import Model

#code to create the windows
window, headFrame, logInFrame, signFrame = SignUp.setupWindow()


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


def loginAttempt(email,password, errorLabel):
    print ("called with " + email +"and" + password)
    if Model.loginAttempt(email, password) == True:
        print ("successfully logged in --> next page")
    else:
        print("error logging in")






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


