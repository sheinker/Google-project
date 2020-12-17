import PySimpleGUI as sg
from online.autoComplete import get_best_k_completions



def searchButton(command):
    result = pg.get_best_k_completions(values[0])
    i = len(result)
    print(f"There are {i} suggestions:")
    for index, item in enumerate(result):
        print(f'{index + 1}. {item.get_completed_sentence()} ({item.get_source_text()} {item.get_offset()})')


sg.theme('lightGreen')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Hello to AutoComplete Search', size=(30, 1))],
          [sg.Text('Enter your text:', size=(15, 1)), sg.InputText(focus=True), sg.Button('Search', bind_return_key=True)],
          # [sg.Output(size=(80, 10))],
          [sg.Output(size=(80, 10))],
          [sg.Button('Cancel')]]


window = sg.Window('AutoComplete', layout)
# pg.read_file()
# pg.init_data()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Search':
        searchButton(values[0])


window.close()















# import PySimpleGUI as sg
# import time
#
# def excecutetest(command):
#         for i in range(5):
#             print (command + str(i))
#             time.sleep(2)
#
# layout = [
#     [sg.Text('Information:', size=(40, 1))],
#     [sg.Output(size=(88, 20))],
#     [sg.Text('Input:', size=(15, 1)), sg.InputText(focus=True), sg.Button('Run', bind_return_key=True)],
#     [sg.Button('EXIT')]
#         ]
#
# window = sg.Window('testing', layout)
#
# # ---===--- Loop taking in user input and using it to call scripts --- #
#
# while True:
#   (event, value) = window.Read()
#   if event == 'EXIT'  or event is None:
#       break # exit button clicked
#   if event == 'Run':
#       excecutetest(value[0])
# window.Close()

