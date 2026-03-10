
import SignUp
import LogIn

#code to create the windows
window, headFrame, mainFrame = SignUp.setupWindow()

#Display log in
LogIn.displayHeader(headFrame)
LogIn.displayLogIn(mainFrame)
#SignUp.displayHeader(headFrame)
#SignUp.displaySignUp(mainFrame)

window.mainloop() #update window

