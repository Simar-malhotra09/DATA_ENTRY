from curses import window
from this import s
from tkinter import EventType, Frame
import PySimpleGUI as sg   
import pandas as pd

EXCEL_FILE = 'Book1.xlsx'
df = pd.read_excel(EXCEL_FILE)
sg.theme('DarkTeal9')
layout = [
    [sg.Text('Please fill the following fields: ')],
    [sg.Text('Name', size =(15,1)), sg.InputText(key="Name")],
    [sg.Text('Username', size = (15,1)), sg.InputText(key = "Username")],
    [sg.Text('Email', size = (15,1,)), sg.InputText(key = "Email")],
    [sg.Text('Mobile Number', size =(15,1)), sg.InputText(key = 'Mobile')],
    [sg.Text('Gender', size = (15,1)), sg.Checkbox('Male', key = 'Male'),
     sg.Checkbox('Female', key = 'Female'),
     sg.Checkbox('Other', key = 'Other')],
    [sg.Text('_'  * 80)],
    [sg.Text('User ID', size = (15,1)), sg.InputText(key ="ID")],
    [sg.Text('User Password', size = (15,1)), sg.InputText(key="Password")],
    
    
    
    [sg.Submit(), sg.Exit(), sg.Button('Clear')]
    
]

window = sg.Window("Customer Creation Form", layout)
def clear():
    for key in values:
        window[key]('')
    return None

while True: 
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup("Data saved!")
        clear()
        
window.close()
    