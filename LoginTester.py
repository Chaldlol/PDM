import PySimpleGUI as sg
import pandas as pd
import glob
import os.path
import io
import os
from datetime import datetime


ACCOUNT_LIST = []
EXCEL_FILE = 'PDM_Accounts.xlsx'
df = pd.read_excel(EXCEL_FILE)

def data_PROGAM():
    print('Program has Finished Login Stage')

def create_Account():
    global username, password
    sg.theme('DarkTeal9')
    layout_CA = [
        [sg.Text('Account Creation', size =(15,1), font=40, justification='c')],
        [sg.Text('Amazon Email', size =(15,1), font=16), sg.InputText(key='-email-', font=16)],
        [sg.Text("Re-enter E-mail", size =(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
        [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
        [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
        [sg.Text("Re-enter Password", size =(15, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
        [sg.Button("Create"), sg.Button("Cancel")]
    ]
    window = sg.Window('Account Creation', layout_CA)

    while True:
        events, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        else:
            if event == 'Create':
                username = values['-username-']
                password = values['-password-']
                ACCOUNT_LIST.append([username,password])
                print(userlist)
    window.close()
create_Account()

def account_Login():
    layout_Login = [
        [sg.Text('Login Screen', size =(15,1), font=40)],
        [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
        [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
        [sg.Button('SIGN UP HERE'),sg.Button('Ok'),sg.Button('Cancel')]
    ]
    window = sg.Window('Login Screen', layout_Login)
while True:
    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    else:
        if event == 'SIGN UP HERE':
            create_Account()
        if event == 'Ok':
            try:
                for c,user in enumerate(userlist):
                    if username in user:
                        print('Finished')
##################                        data_PROGAM()
                    else:
                        print("Incorrect password")
                else:
                    if c != len(userlist):
                        pass
                    else:
                        print("Unregistered username")
##################                        mainpage()
