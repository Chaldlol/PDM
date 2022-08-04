import PySimpleGUI as sg
import pandas as pd
import glob
import os.path
import io
from PIL import Image
from datetime import datetime
import os
#       IF LOCATION == ANY OF THESE THEN COMPONENTS == THAT
#       OB1-1=eightComp
#       OB1-2,OB1-4, OB2-1, OB2-3, OB3-1, OB3-3, OB4-1, TH-1=sevenComp
#       OB3-5=fiveComp
#       OB1-4A, OB1-5, OB3-6, OB3-8=fourComp
#       OB3-2, OB3-4, OB3-7=twoComp
eightComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'MOTOR']
sevenComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'MOTOR']
fiveComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'R1', 'R2', 'R3', 'R4', 'R5', 'MOTOR']
fourComp = ['L1', 'L2', 'L3', 'L4', 'R1', 'R2', 'R3', 'R4', 'MOTOR']
twoComp = ['L1', 'L2', 'R1', 'R2', 'MOTOR']
myTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
imgDir = ['C:/Users/chartze/Desktop/pDm/Photo/Photo2/*.png/']
componentDir = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'MOTOR']
# Add some color to the window
sg.theme('DarkTeal9')
EXCEL_FILE = 'Tester.xlsx'
df = pd.read_excel(EXCEL_FILE)

data_form_column = [
    [sg.Text('Please Fill Out The Following Fields:')],
    [sg.Text('TimeStamp', size=(10,1)), sg.Input(default_text = myTime, visible = False, key='TimeStamp'), sg.Checkbox('LoginLock', enable_events=True, key='LockMe')],
    [sg.Text('Login', size=(10,1)), sg.Combo(['Chartze', 'Jon1', 'Jon2', 'JonFree', 'Yes'], enable_events=True, key='Login')],
    [sg.Text('Location', size=(10,1)), sg.Combo(['OB1-1 _14JK72', 'OB1-2_14JK73', 'OB1-4_14JK75', 'OB1-4A_14JK76', 'OB1-5_14JK85', 'OB2-1_14JK77', 'OB2-3_14JK79', 'OB3-1_14JK80', 'OB3-2_14JK81', 'OB3-3_14JK82', 'OB3-4_14JK83', 'OB3-5_14JK84', 'OB3-6_14JK86', 'OB3-7_14JK87', 'OB3-8_14JK88', 'OB4-1_14JK90', 'TH-1_14JG05'], key='Location')],
#    [sg.Text('Component', size=(10,1)), sg.Combo(['L1', 'L2', 'R1', 'R2', 'Motor'], key='Component')],
    [sg.Text('H-VeL', size=(10,1)), sg.InputText(size=(10,1), key='H-VeL')],
    [sg.Text('V-VeL', size=(10,1)), sg.InputText(size=(10,1), key='V-VeL')],
    [sg.Text('A-VeL', size=(10,1)), sg.InputText(size=(10,1), key='A-VeL')],
    [sg.Text('H-GE', size=(10,1)), sg.InputText(size=(10,1), key='H-GE')],
    [sg.Text('V-GE', size=(10,1)), sg.InputText(size=(10,1), key='V-GE')],
    [sg.Text('A-GE', size=(10,1)), sg.InputText(size=(10,1), key='A-GE')],
    [sg.Text('Temp', size=(10,1)), sg.InputText(size=(10,1), key='Temp')],
    [sg.Text('Belt Tracking', size=(10,1)), sg.Combo(['Perfection', 'Functional', 'Close to Wall', 'Belt Rubbing Wall', 'Details In Comments'], key='BeltTracking')],
    [sg.Text('Comments', size=(10,1)), sg.Multiline(size=(23,3), key='Comments')],
    [sg.Submit('Submit', pad=(0,0,0)), sg.Button('Clear', pad=(75,0,0)), sg.Exit()]
]
# First the window layout in 2 columns

file_list_column = [
    [sg.Text("Location", size=(10,1))],
    [sg.In(size=(10, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse(initial_folder = imgDir)],
    [sg.Listbox(values=[], enable_events=True, size=(12,17), key="-FILE LIST1-")],
    [sg.Text("Component", size=(10,1))],
    [sg.Listbox(values=componentDir, enable_events=True, size=(12,17), key='Component')],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose a Location from list1 on left:")],
    [sg.Text(size=(40, 1), key="-TOUT1-")],
    [sg.Image(key="-IMAGE1-")],
    [sg.Text('Choose a Component from list2 on left:')],
    [sg.Text(size=(40,1), key='-TOUT1-')],
    [sg.Image(key="-IMAGE1-")],
]

# This is the List Box layout
audit_box_row = [
        [sg.Text('Audit Your Work', size=(15,1))],
        [sg.Listbox([], size=(100, 20), auto_size_text=True,  enable_events=True, key='audit_box_row')],
        [sg.Button('Update', pad=(5,0,0), enable_events=True, key='UPDATEME'), sg.Button('!Send It!', pad=(50,0,0), enable_events=True, key='SENDME'), sg.Button('Delete', pad=(100,0,0), enable_events=True, key='DELETEME')],
]

#layout = [
#        [sg.vtop(data_form_column, file_list_column, [image_viewer_column]), [audit_box_row]]
#]
layout = [
    [
        sg.Column(data_form_column),
        sg.VSeperator(),
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(audit_box_row),
    ]
]

window = sg.Window('Simple data entry form', layout)


def clear_input():
    for key in values:
        if key == 'Login':
            continue
        window[key]('')
    return None

def field_Lock():
    for key in values:
        if key == 'Lockme':
            values[Login](readonly=True)
    return None

def audit_add():
    event, values = window.read()
    for key in values:
        window['audit_box_row'].update([values])
        if window[key] == '':
            continue
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Lockme':
        field_Lock()
    if event =='Location':
        img_Viewer()
    if event == 'Clear':
        clear_input()
    if event == 'UPDATEME':
        update_input()
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST1-"].update(fnames)
    elif event == "-FILE LIST1-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST1-"][0]
            )
#            filename2 = os.path.join(values["-FOLDER-"], values["-FILE LIST1-"][0])
            window["-TOUT1-"].update(filename)
            window["-IMAGE1-"].update(filename=filename)
#            window["-TOUT1-"].update(filename2)
#            window["IMAGE1-"].update(filename2=filename2)

        except:
            pass

    elif event == 'Submit':
        audit_add()
#        new_record = pd.DataFrame(values, index=[0])
#        df = pd.concat([df, new_record], ignore_index=True)
#        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
#        clear_input()
window.close()
