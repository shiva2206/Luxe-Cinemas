import PySimpleGUI as sg
from os import startfile
lt1=[[sg.Image('eeswaran.png')], [sg .T('eeswaran')],
                                 [sg.B('proceed')]]
win1=sg.Window('eeswaran',lt1)
v1=1
while v1==1:
    event,values=win1.read()
    if event==sg.WIN_CLOSED:
        win1.close()
        v1=2
    elif event=='proceed':
        lt2=[[sg.Image('eeswaran(2).png')], [sg .T('eeswaran')],
                                     [sg.B('watch trailer')]]
        win2=sg.Window('eeswaran',lt2)                         
        v1=2
        v2=1
        while v2==1:
            event,values=win2.read()
            if event==sg.WIN_CLOSED:
                win2.close()
                v2=2
                v1=1
            elif event=='watch trailer':
                v1=2
                win1.close()
                startfile('eeswaran trailer.mp4')
