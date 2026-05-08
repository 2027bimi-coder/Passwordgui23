import tkinter as tk
from tkmacosx import Button
import pathlib, os

#When user clicks inside a text box, delet the placeholder text
def clearEntry(*args):
    entryBox = args[1]
    entryBox.delete(0, "end")


#Displaying lables (where everything should go)
def displayHeader(headFrame, goBack):
    """
    Adds the back arrow and top label for the header frame + displays header
    """
    headLabel = tk.Label(master=headFrame, text="Log in", bg="#2699FB", height=3)
    headLabel.grid(row=0, column=1, padx=10, sticky="nsew")

    # display frame
    headFrame.grid(row=0, column=0, sticky="ew", columnspan=3)

def setUpLogIn(LogInFrame, signUpPage, loginAttempt, passwordResetEmail):
    """
    Adds all elements for the main frame of signup screen and displays the frame
    """
    # add elements
    # Email label and textbox
    emailLabel = tk.Label(master=LogInFrame, text="Email:", fg="#000000", bg="#FAFAFA", height=3)
    emailLabel.grid(row=1, column=0, columnspan=3, padx=10, sticky="w")
    emailText = tk.StringVar()
    emailText.set("Enter your Email")
    emailBox = tk.Entry(master=LogInFrame, width=30, font=('calibre', 18, 'normal'),
                       textvariable=emailText, bg="#FFFFFF", fg="#2699FB",
                       highlightthickness=1, relief="flat", highlightcolor="#2699FB",
                       highlightbackground="#2699FB")
    emailBox.grid(row=2, column=0, columnspan=3, padx=30, sticky="w")
    #Bind function to email box (when the user clicks this box, run clearEntry)
    emailBox.bind("<FocusIn>", lambda event: clearEntry(event, emailBox))

    # Password initial label, textbox and settings
    passwordLabel = tk.Label(master=LogInFrame, text="Enter your password:", fg="#000000", bg="#FAFAFA", height=3)
    passwordLabel.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")
    passwordText = tk.StringVar()
    passwordText.set("Enter your Password")
    passwordBox = tk.Entry(master=LogInFrame, width=30, font=('calibre', 18, 'normal'),
                        textvariable=passwordText, bg="#FFFFFF", fg="#2699FB",
                           show="*",
                        highlightthickness=1, relief="flat", highlightcolor="#2699FB",
                        highlightbackground="#2699FB")
    passwordBox.grid(row=4, column=0, columnspan=3, padx=30, sticky="w")
    passwordBox.bind("<FocusIn>", lambda event: clearEntry(event, passwordBox))
    # display frame
    LogInFrame.grid(row=1, column=0, columnspan=3, rowspan=15, sticky="nsew")

    #error message (starts off as empty,
    # if log in fail, set text to show error message
    errorLabel = SignInLabel = tk.Label(master=LogInFrame, text="",
                             cursor="hand2", fg="#FF0000", bg="#FAFAFA", height=3)
    errorLabel.grid(row=15, column=0, columnspan=3)
    SignInLabel.grid(row=5, column=0, columnspan=3, padx=10, sticky="ew")


    # forgot password label
    ForgotpwLabel = tk.Label(master=LogInFrame, text="Forgot Password?", font = ("Arial", 10, "underline"), cursor = "hand2", fg="#2699FB", bg="#FAFAFA", height=1)
    ForgotpwLabel.grid(row=6, column=1, columnspan=3, padx=10, sticky="w")
    #connect to Button-1, so when clicked call passwordResetEmail function
    ForgotpwLabel.bind("<Button-1>", lambda event:passwordResetEmail(event, emailText.get(), errorLabel))
    # Submit button
    #--> call loginAttempt() when ckicked
    submit = Button(master=LogInFrame, width=31, bg="#2699FB", text="Submit", borderless=1, fg="#FFFFFF",
                    command=lambda:loginAttempt(emailText.get(), passwordText.get(), errorLabel))

    submit.grid(row=8, pady=20, column=0, columnspan=3, sticky="nsew")


    # sign up section (make label for if user does not have an account)
    SignUpLabel = tk.Label(master=LogInFrame, text="Don't have an Account? Sign up", font=("Arial", 16, "underline"),
                             cursor="hand2", fg="#2699FB", bg="#FAFAFA", height=3)
    SignUpLabel.grid(row=9, column=0, columnspan=3, padx=10, sticky="ew")
    #calls signUpPage() to switch screens if no account
    SignUpLabel.bind("<Button-1>", signUpPage)

    return LogInFrame

def displayLogUp(LogInFrame, headFrame):
    displayHeader(headFrame, None)
    LogInFrame.grid(row=1, column=0, columnspan=3, rowspan=15, sticky="nsew")

def hideLogIn(LogInFrame, headFrame, passwordResetEmail):
    LogInFrame.grid_forget()

    for widget in headFrame.winfo_children():
            widget.destroy()

def colorValidLabel(vLabel):
    vLabel.config(fg="#00BC16")

def colorInvalidLabel(vLabel):
    vLabel.config(fg="#F20847")

def UpdateLabelText(vLabel, text):
    vLabel.config(text=text)