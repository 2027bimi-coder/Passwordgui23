
import SignUp
import LogIn

#code to create the windows
window, headFrame, logInFrame, signUpFrame = SignUp.setupWindow()

#Display log in
LogIn.displayHeader(headFrame)
LogIn.setUpLogIn(logInFrame)
#SignUp.displayHeader(headFrame)
#SignUp.displaySignUp(mainFrame)

window.mainloop() #update window


