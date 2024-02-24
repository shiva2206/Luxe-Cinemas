import PySimpleGUI as sg
import pandas as pd

employee=pd.read_csv("movie employee.csv")
employee=employee.set_index("id")
c=0
while  c<1: 
    layout=[[sg.Button("ADMIN(owner)")],
            [sg.Button("manager")],
            [sg.Button("counter")],
            [sg.Button("employee")],
            [sg.Button("close")]]
    window=sg.Window("details",layout)
    event,vals = window.read()
    window.close()
    d=0
    while d<1:
         if event=="ADMIN(owner)":
             layout=[[sg.Text("name")],[sg.Input()],
                     [sg.Text("password")],[sg.Input()],
	             [sg.Button("submit")],[sg.Button("back")]]
             window=sg.Window("details",layout)
             event,vals = window.read()
             window.close()
             name=vals[0]
             password=vals[1]
             
             if event=="back":
                 e=1
                 d=1    
             elif event=="submit":
                 for i in employee.values:
                     e=0
                     while e<1:
                        if str(i[0])==str(name) and str(i[-1])==str(password):
                                layout=[[sg.Button("re-set MYdetails")],
                                        [sg.Button("view bookingscreen")],
                                        [sg.Button("employee table")],
                                        [sg.Button("movieshow INFO")],
	                                [sg.Button("clos"),sg.Button("log out")]]
                                window=sg.Window("details",layout)
                                event,vals = window.read()
                                window.close()
                                if event=="log out":
                                    d=d-1
                                    c=c-1
                                    e=1
                                elif event=="re-set MYdetails":
                                    sg.popup("current details")
                                             
                        e=e+1            
         elif event=="manager":
             
             layout=[[sg.Text("name")],[sg.Input()],
                     [sg.Text("password")],[sg.Input()],
	             [sg.Button("submit")],[sg.Button("back")]]
             window=sg.Window("details",layout)
             event,vals = window.read()
             window.close()
             name=vals[0]
             password=vals[1]
             if event=="back":
                 e=1
                 d=1
             elif event=="submit":
                 for i in employee.values:
                     e=0
                     while e<1:
                        if str(i[0])==str(name) and str(i[6])==str(password):
                                layout=[[sg.Button("A")],
                                        [sg.Button("view bookingscreen")],
                                        [sg.Button("employee table")],
                                        [sg.Button("movieshow INFO")],
	                                [sg.Button("back")]]
                                window=sg.Window("details",layout)
                                event,vals = window.read()
                                window.close()
                                if event=="back":
                                    d=d-1
                                    c=c-1
                                    e=1
                        e=e+1             
         elif event=="counter":
             layout=[[sg.Text("name")],[sg.Input()],
                     [sg.Text("password")],[sg.Input()],
	             [sg.Button("submit")],[sg.Button("back")]]
             window=sg.Window("details",layout)
             event,vals = window.read()
             window.close()
             name=vals[0]
             password=vals[1]
             if event=="back":
                 e=1
                 d=1
             elif event=="submit":
                 for i in employee.values:
                     e=0
                     while e<1:
                        if str(i[0])==str(name) and str(i[6])==str(password):
                                layout=[[sg.Button("A")],
                                        [sg.Button("Book Ticket")],
                                        [sg.Button("employee table")],
                                        [sg.Button("movieshow INFO")],
	                                [sg.Button("back")]]
                                window=sg.Window("details",layout)
                                event,vals = window.read()
                                window.close()
                                if event=="back":
                                    d=d-1
                                    c=c-1
                                    e=1
                        e=e+1             
         elif event=="employee":
             layout=[[sg.Text("name")],[sg.Input()],
                     [sg.Text("password")],[sg.Input()],
	             [sg.Button("submit")],[sg.Button("back")]]
             window=sg.Window("details",layout)
             event,vals = window.read()
             window.close()
             name=vals[0]
             password=vals[1]
             if event=="back":
                 e=1
                 d=1
             elif event=="submit":
                 for i in employee.values:
                     e=0
                     while e<1:
                        if str(i[0])==str(name) and str(i[6])==str(password):
                                layout=[[sg.Button("A")],
                                        [sg.Button("Book Ticket")],
                                        [sg.Button("employee table")],
                                        [sg.Button("movieshow INFO")],
	                                [sg.Button("back")]]
                                window=sg.Window("details",layout)
                                event,vals = window.read()
                                window.close()
                                if event=="back":
                                    d=d-1
                                    c=c-1
                                    e=1
                        e=e+1             
         d=d+1  
    c=c+1 
