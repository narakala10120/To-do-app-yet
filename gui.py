
import functions


import PySimpleGUI as sg

input_box = sg.InputText(tooltip='Enter your todo for the day')
label = sg.Text('Type in a todo')

window = sg.Window('To-do App', layout=[[label,input_box]])
window.read()
window.close()