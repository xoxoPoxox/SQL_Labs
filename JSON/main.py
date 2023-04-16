import json
import PySimpleGUI as sg

sg.theme('LightPurple')
first_list_column = [


    [
        sg.Text("Строка:"),
        sg.In(size=(15,1), enable_events=True, key="-Atext-"),
        sg.Button("Добавить", enable_events=True, key="-AddJson-"),
    ],

    [
        sg.Text("Строка:"),
        sg.In(size=(15, 1), enable_events=True, key="-Utext-"),
        sg.Button("Изменить", enable_events=True, key="-UpdateJson-"),
    ],
[
        sg.Button("Показать", enable_events= True, key="-ShowJson-")
    ]
]
second_list_column = [
    [
        sg.Text(text=" ", key="-Text-")
    ]
]
layout = [
    [
        sg.Column(first_list_column,element_justification='c', size=(350, 700), scrollable=False),
        sg.VSeparator(),
    sg.Column(second_list_column, size =(900, 400), scrollable=True),
        sg.VSeparator()
    ]
]
window = sg.Window("JSON", layout, size=(1050, 400))
sg.theme('LightPurple')

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-AddJson-":
        try:
            data = values["-Atext-"]
            y, m, day, p, c = map(int, data.split(" "))
            print(y, m, day, p, c)
            d = json.load(open('main_json.json'))
            d["values"] += list(({"date": {"year": y, "month": m, "day": day}, "pay": p, "cons": c}, ))
            json.dump(d, open('main_json.json', 'w'))

        except:
            pass
    if event == "-UpdateJson-":
        try:
            data = values["-Utext-"]
            d = json.load(open('main_json.json'))
            num, z = map(int, data.split(" "))
            zn = int(z)
            #d["values"][num].get("pay") = z
            del d["values"][num]["pay"]
            d["values"][num]["pay"] = z
            json.dump(d, open('main_json.json', 'w'))
        except:
            pass
    if event == "-ShowJson-":
        try:
            d = json.load(open('main_json.json'))
            print(d)
            result = str(d)
            #print(result)
            window["-Text-"].update(result.replace("}, {", "\n"))
        except:
            pass