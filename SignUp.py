import tkinter as tk
from tkmacosx import Button
import pathlib, os
#from tkcalendar2 import tkcalendar

def clearEntry(event, entryBox):
    entryBox.delete(0, "end")

def setupWindow():
    """
    Create and setup the window, including frames for header and main page
    :return:
        window -- the full window for the application,
        headFrame -- a frame for the page header
        mainFrame -- the frame for the main portion of the page
    """
    # create window & update size / title
    window = tk.Tk(className="Password Project")
    window.geometry("399x864")  # 3 x 16grid

    # configure layout
    for c in range(0,3):
        window.columnconfigure(c, weight=1, minsize=100)
    weights=[1,1,1,1,1,1,1,1,1,3,1,1,2]
    for r in range(0,13):
        window.rowconfigure(r, weight=weights[r], minsize=50)

    # create a frame for the header
    headFrame = tk.Frame(master=window, bg="#2699FB")
    headFrame.columnconfigure([0,1,2], weight=1, minsize=100)

    # create frame for sign-up screen
    signUpFrame = tk.Frame(bg="#FAFAFA")
    logInFrame = tk.Frame(bg="#FAFAFA")

    return window, headFrame, signUpFrame, logInFrame

def displayHeader(headFrame, goBack):
    """
    Adds the back arrow and top label for the header frame + displays header
    """
    # find full image path
    img_file_name = "arrow.png"
    current_dir = pathlib.Path(__file__).parent.resolve()  # current directory
    img_path = os.path.join(current_dir, img_file_name)
    # add elements
    imgArw=tk.PhotoImage(file=img_path)
    imgArwLabel = tk.Label(master=headFrame, image=imgArw, bg="#2699FB")
    imgArwLabel.image = imgArw
    imgArwLabel.grid(row=0, column=0, sticky="w")

    headLabel = tk.Label(master=headFrame, text="Sign Up", bg="#2699FB", height=3)
    headLabel.grid(row=0, column=1, padx=10, sticky="nsew")

    # display frame
    headFrame.grid(row=0, column=0, sticky="ew", columnspan=3)
    if callable(goBack):
        imgArwLabel.bind("<Button-1>", goBack)

def setUpSignUp(signFrame, headFrame, validatePW, submitAttempt, goBack):
    """
    Adds all elements for the main frame of signup screen and displays the frame
    """
    displayHeader(headFrame, goBack)
    # add elements


    # Name label and textbox
    nameLabel = tk.Label(master=signFrame, text="Full Name", fg="#000000", bg="#FAFAFA", height=3)
    nameLabel.grid(row=1, column=0, columnspan=3, padx=10, sticky="w")
    nameText = tk.StringVar()
    nameText.set("enter your full name")
    nameBox = tk.Entry(master=signFrame, width=30, font=('calibre',18,'normal'),
                       textvariable=nameText, bg="#FFFFFF",  fg="#2699FB",
                       highlightthickness=1, relief="flat",highlightcolor="#2699FB",
                       highlightbackground="#2699FB")
    nameBox.grid(row=2, column=0, columnspan=3, padx=30, sticky="w")
    nameBox.bind("<FocusIn>", lambda event: clearEntry(event, nameBox))

    # email label and textbox
    emailLabel = tk.Label(master=signFrame, text="Email", fg="#000000", bg="#FAFAFA", height=3)
    emailLabel.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")
    emailText = tk.StringVar()
    emailText.set("Enter Email")
    emailBox = tk.Entry(master=signFrame, width=30, font=('calibre', 18, 'normal'),
                       textvariable=emailText, bg="#FFFFFF", fg="#2699FB",
                       highlightthickness=1, relief="flat",highlightcolor="#2699FB",
                       highlightbackground="#2699FB")
    emailBox.grid(row=4, column=0, columnspan=3, padx=30, sticky="w")
    emailBox.bind("<FocusIn>", lambda event: clearEntry(event, emailBox))
    # password label and textbox
    pwLabel = tk.Label(master=signFrame, text="Password", fg="#000000", bg="#FAFAFA", height=3)
    pwLabel.grid(row=5, column=0, columnspan=3, padx=10, sticky="w")
    pwText = tk.StringVar()
    pwText.set("Enter Password")
    pwBox = tk.Entry(master=signFrame, width=30, font=('calibre', 18, 'normal'),
                        textvariable=pwText, bg="#FFFFFF", fg="#2699FB",
                        show="*",
                        highlightthickness=1, relief="flat",highlightcolor="#2699FB",
                        highlightbackground="#2699FB")
    pwBox.grid(row=6, column=0, columnspan=3, padx=30, sticky="w")
    pwBox.bind("<FocusIn>", lambda event: clearEntry(event, pwBox))

    # confirm password label and textbox
    pwConLabel = tk.Label(master=signFrame, text="Confirm Password", fg="#000000", bg="#FAFAFA", height=3)
    pwConLabel.grid(row=7, column=0, columnspan=3, padx=10, sticky="w")
    pwConText = tk.StringVar()
    pwConText.set("Enter Password")
    pwConBox = tk.Entry(master=signFrame, width=30, font=('calibre', 18, 'normal'),
                     textvariable=pwConText, bg="#FFFFFF", fg="#2699FB",
                     highlightthickness=1, relief="flat",highlightcolor="#2699FB",
                        show="*",
                     highlightbackground="#2699FB")
    pwConBox.grid(row=8, column=0, columnspan=3, padx=30, sticky="w")
    pwConBox.bind("<FocusIn>", lambda event: clearEntry(event, pwConBox))
    # Password parameters (matching, length >= 8, contains special character)

    pwMatchLabel = tk.Label(master=signFrame, text="Passwords must match",
                            fg="#00BC16", bg="#FAFAFA")
    pwMatchLabel.grid(row=9, column=0, columnspan=3, padx=50, sticky="w")

    pwLengthLabel = tk.Label(master=signFrame, text="Passwords must be at least 8 characters long",
                             fg="#F20847", bg="#FAFAFA")
    pwLengthLabel.grid(row=10, column=0, columnspan=3, padx=50, sticky="w")

    pwCharLabel = tk.Label(master=signFrame, text="Passwords must include a special character",
                           fg="#F20847",bg="#FAFAFA")
    pwCharLabel.grid(row=11, column=0, columnspan=3, padx=50, sticky="w")

    pwText.trace_add("write",
                     lambda *args, confirmPassword=pwConText, labels=[pwMatchLabel, pwLengthLabel, pwCharLabel],
                            password=pwText: validatePW(*args, password, confirmPassword, labels))
    pwConText.trace_add("write", lambda *args, password=pwText, labels=[pwMatchLabel, pwLengthLabel, pwCharLabel],
                                        confirmPassword=pwConText: validatePW(*args, password, confirmPassword, labels))

    # Birthdate label and date entry
    bDayLabel = tk.Label(master=signFrame, text="Birthdate ", fg="#000000", bg="#FAFAFA", height=3)
    bDayLabel.grid(row=12, column=0, columnspan=3, padx=10, sticky="w")
   # cal = tkcalendar.Calendar(master=signFrame)
    #cal.grid(row=13, column=0, columnspan=2, padx=30, sticky="w")

    dateLabel = tk.Label(master=signFrame, text="Select a date", fg="#2699FB", bg="#FAFAFA", height=3)
    dateLabel.grid(row=13, column=2, padx=10, sticky="w")

    #error message
    errorLabel = SignInLabel = tk.Label(master= signFrame, text="",)
    errorLabel.grid(row=15, column=0, columnspan=3)
    errorLabel.bind("<Button-1>", lambda event: errorLabel.config(text=""))

    # Submit button
    submit = submit = Button(
    master=signFrame,
    width=31,
    bg="#2699FB",
    text="Submit",
    borderless=1,
    fg="#FFFFFF",
    command=lambda: submitAttempt(nameText.get(), emailText.get(), pwText.get(), errorLabel))
    submit.grid(row=14, pady=20, column=0, columnspan=3, sticky="nsew")

    return signFrame

def displaySignUp(signFrame, headFrame, goBack):
    displayHeader(headFrame, goBack)

    signFrame.grid(row=1, column=0, columnspan=3, rowspan=15, sticky="nsew")
    signFrame.update_idletasks()

def hideSignUp(signFrame, headFrame):
    headFrame.grid_forget()

    for widget in headFrame.winfo_children():
        widget.destroy()


def colorValidLabel(vLabel):
    vLabel.config(fg="#00BC16")

def colorInvalidLabel(vLabel):
    vLabel.config(fg="#F20847")

