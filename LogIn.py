import tkinter as tk
from tkmacosx import Button
import pathlib, os

def displayHeader(headFrame):
    """
    Adds the back arrow and top label for the header frame + displays header
    """

    headLabel = tk.Label(master=headFrame, text="Log in", bg="#2699FB", height=3)
    headLabel.grid(row=0, column=1, padx=10, sticky="nsew")

    # display frame
    headFrame.grid(row=0, column=0, sticky="ew", columnspan=3)

def displayLogIn(LogInFrame):
    """
    Adds all elements for the main frame of signup screen and displays the frame
    """
    # add elements

    # Name label and textbox
    emailLabel = tk.Label(master=LogInFrame, text="Email:", fg="#000000", bg="#FAFAFA", height=3)
    emailLabel.grid(row=1, column=0, columnspan=3, padx=10, sticky="w")
    emailText = tk.StringVar()
    emailText.set("2027bimi@seisen.com")
    emailBox = tk.Entry(master=LogInFrame, width=30, font=('calibre', 18, 'normal'),
                       textvariable=emailText, bg="#FFFFFF", fg="#2699FB",
                       highlightthickness=1, relief="flat", highlightcolor="#2699FB",
                       highlightbackground="#2699FB")
    emailBox.grid(row=2, column=0, columnspan=3, padx=30, sticky="w")

    # display frame
    LogInFrame.grid(row=1, column=0, columnspan=3, rowspan=15, sticky="nsew")



    passwordLabel = tk.Label(master=LogInFrame, text="Email:", fg="#000000", bg="#FAFAFA", height=3)
    passwordLabel.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")
    passwordText = tk.StringVar()
    passwordText.set("2027bimi@seisen.com")
    passwordBox = tk.Entry(master=LogInFrame, width=30, font=('calibre', 18, 'normal'),
                        textvariable=passwordText, bg="#FFFFFF", fg="#2699FB",
                        highlightthickness=1, relief="flat", highlightcolor="#2699FB",
                        highlightbackground="#2699FB")
    passwordBox.grid(row=3, column=0, columnspan=3, padx=30, sticky="w")

    # display frame
    LogInFrame.grid(row=4, column=0, columnspan=3, rowspan=15, sticky="nsew")
