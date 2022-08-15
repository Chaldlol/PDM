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

# dictionary example for you to fix
ob_comp_dict = dict()
ob_comp_dict = {
    'OB1' : ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'M'],
    'OB2' : ['L1', 'L2', 'R1', 'R2', 'M'],
    'OB3' :  ['L1', 'L2', 'L3', 'L4', 'R1', 'R2', 'R3', 'R4', 'M']
}
print(ob_comp_dict) # prints your WHOLE dictionary. 

ob_comp_dict['OB1'] # will access the list stored in OB1 

print(ob_comp_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))

# End dictionary example 


# Components
eightComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'M']
sevenComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'M']
fiveComp = ['L1', 'L2', 'L3', 'L4', 'L5', 'R1', 'R2', 'R3', 'R4', 'R5', 'M']
fourComp = ['L1', 'L2', 'L3', 'L4', 'R1', 'R2', 'R3', 'R4', 'M']
twoComp = ['L1', 'L2', 'R1', 'R2', 'M']



myTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
componentDir = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'M']
imgDir = ['C:/Users/chartze/Desktop/pDm/Photo/Photo2/*.png/']
# TODO Look into using os.getcwd() to get the current working directory of the running script. 

# Add some color to the window
sg.theme('DarkTeal9')
EXCEL_FILE = 'Tester.xlsx'
df = pd.read_excel(EXCEL_FILE)

data_form_column = [
    [sg.Text('Please Fill Out The Following Fields:')],
    [sg.Input(default_text = myTime, visible = False, key='TimeStamp')],
    [sg.Text('Login', size=(10,1)), sg.Combo(['Chartze', 'Jon1', 'Jon2', 'JonFree', 'Yes'], enable_events=True, key='Login')],
    [sg.Text('Location', size=(10,1)), sg.Combo(['OB1-1', 'OB1-2', 'OB1-4', 'OB1-4A', 'OB1-5', 'OB2-1', 'OB2-3', 'OB3-1', 'OB3-2', 'OB3-3', 'OB3-4', 'OB3-5', 'OB3-6', 'OB3-7', 'OB3-8', 'OB4-1', 'TH-1'], key='Location')],
#    [sg.Text('Component', size=(10,1)), sg.Combo(['L1', 'L2', 'R1', 'R2', 'Motor'], key='Component')],
    [sg.Text('H-VeL', size=(5,1)), sg.InputText(size=(5,1), key='H-VeL'), sg.Text('V-VeL', size=(5,1)), sg.InputText(size=(5,1), key='V-VeL'), sg.Text('A-VeL', size=(5,1)), sg.InputText(size=(5,1), key='A-VeL')],
    [sg.Text('H-GE', size=(5,1)), sg.InputText(size=(5,1), key='H-GE'), sg.Text('V-GE', size=(5,1)), sg.InputText(size=(5,1), key='V-GE'), sg.Text('A-GE', size=(5,1)), sg.InputText(size=(5,1), key='A-GE')],
    [sg.Text('Temp', size=(10,1)), sg.InputText(size=(10,1), key='Temp')],
    [sg.Text('Belt Tracking', size=(10,1)), sg.Combo(['Perfection', 'Functional', 'Close to Wall', 'Belt Rubbing Wall', 'Details In Comments'], key='BeltTracking')],
    [sg.Text('Comments', size=(10,1)), sg.Multiline(size=(23,3), key='Comments')],
    [sg.Submit('Submit', pad=(0,0,0)), sg.Button('Clear', pad=(75,0,0)), sg.Exit()]
]
# First the window layout in 2 columns

file_list_column = [
    [sg.Text("Location Maps", size=(10,1))],
    [sg.In(size=(10, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse(initial_folder = imgDir)],
    [sg.Listbox(values=[], enable_events=True, size=(12,5), key="-FILE LIST1-")],
    [sg.Text("Components", size=(10,1))],
    [sg.Listbox(values=componentDir, enable_events=True, size=(12,5), key='Component')],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose a Location from list1 on left:")],
    [sg.Text(size=(20, 1), key="-TOUT1-")],
    [sg.Image(key="-IMAGE1-")],
#    [sg.Text('Choose a Component from list2 on left:')],
#    [sg.Text(size=(40,1), key='-TOUT1-')],
#    [sg.Image(key="-IMAGE1-")],
]

# This is the List Box layout
audit_box_column = [
        [sg.Text('Audit Your Work', size=(15,1))],
        [sg.Listbox([], horizontal_scroll=True, auto_size_text=True,  enable_events=True, key='audit_box_row')],
        [sg.Button('Update', pad=(5,0,0), enable_events=True, key='UPDATEME'), sg.Button('!Send It!', pad=(25,0,0), enable_events=True, key='SENDME'), sg.Button('Delete', pad=(25,0,0), enable_events=True, key='DELETEME')],
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
        sg.Column(audit_box_column),
    ]
]

window = sg.Window('Data Entry Form', layout)

def clear_input():
    for key in values:
        if key == 'Login' or 'Location' or 'audit_box_row':
            continue
        else:
            window[key]('')

def audit_add():
    while True:
        event, values = window.read()
        window['audit_box_row'].update(values['TimeStamp'], ['Login'], ['Location'], ['Component'], ['H-VeL'], ['V-VeL'], ['A-VeL'], ['H-GE'], ['V-GE'], ['A-GE'], ['Temp'], ['BeltTracking'], ['Comments'],)

#def audit_add():
#    event, values = window.read()
#    for key in values:
#        window['audit_box_row'].update('Location', 'Component', 'H-VeL', 'V-VeL', 'A-VeL', 'H-GE', 'V-GE', 'A-GE', 'Temp', 'BeltTracking', 'Comments')
#        if window[key] == '':
#            continue
#    return None
#
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event =='Location':
        img_Viewer()
    if event == 'Clear':
        clear_input()
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
            window["-TOUT1-"].update(filename)
            window["-IMAGE1-"].update(filename=filename)
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
