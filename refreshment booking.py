import PySimpleGUI as sg
import pandas as pd
import datetime
import random as rd
def unique_value(dataframe,column):
    lt=[]
    for var in dataframe[column]:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)



sunny=0
while sunny<1:
                                                                                                                                          refreshments=pd.read_csv("movie refreshments.csv")
                                                                                                                                          refreshments=refreshments.set_index("id")
                                                                                                                                          
                                                                                                                                          uniquesnackstype=unique_value(refreshments,"type")
                                                                                                                                          uniquesnacksimage=unique_value(refreshments,"image")                                 
                                                                                                                                          
                                                                                                                                          textsnackstype=[]
                                                                                                                                          imagesnacksimage=[]
                                                                                                                                          snacksbutton=[]
                                                                                                                                          for tip in range(len(uniquesnackstype)):
                                                                                                                                               textsnackstype.append(sg.T(uniquesnackstype[tip]))
                                                                                                                                               imagesnacksimage.append(sg.T(uniquesnacksimage[tip]))
                                                                                                                                               snacksbutton.append(sg.B(uniquesnackstype[tip]))
                                                                                                                                          orderedsnacksname=[]                                            
                                                                                                                                          orderedsnacksprice=[]
                                                                                                                                          orderedsnacksquantity=[]                                                                                               

     
                                                                                                                                                                   
                                                                                                                                          maalu=0                              
                                                                                                                                          while maalu<1:
                                                                                                                                                  if len(orderedsnacksname)==0:
                                                                                                                                                          forwardbutton=[sg.T(" ")]                  
                                                                                                                                                  else:
                                                                                                                                                          forwardbutton=[sg.B("NEXT")]
                                                                                                                                                  print("to")        
                                                                                                                                                  snackswindow=[[sg.T("-------REFRESHMENTS---------")],
                                                                                                                                                                textsnackstype,
                                                                                                                                                                imagesnacksimage,
                                                                                                                                                                snacksbutton,
                                                                                                                                                                forwardbutton]
                                                                                                                                                  item,values=sg.Window(" k",snackswindow,default_button_element_size=(3,1), auto_size_buttons=False)
                                                                                                                                                  snackswindow.read()
                                                                                                                                                  snackswindow.close()

                                                                                                                                                  snacksname=[]
                                                                                                                                                  
                                                                                                                                                  snacksprice=[]
                                                                                                                                                  chatbutton=[]
                                                                                                                                                  refreshmentsname=[]

                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  for yoyo in uniquesnackstype:
                                                                                                                                                          if item==yoyo:
                                                                                                                                
                                                                                                                                                                  refreshments=refreshments[refreshments.type==item]
                                                                                                                                                  for jog in refreshments.index:                                                                               
                                                                                                                                                                          snacksname.append(sg.T(refreshments.loc[jog]["item"],size=(3,1)))
                                                                                                                                                                          snacksprice.append(sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(3,1)))
                                                                                                                                                                          chatbutton.append(sg.B("ADD",key=refreshments.loc[jog]["item"],size=(3,1)))
                                                                                                                                                                          refreshmentsname.append(refreshments.loc[jog]["item"])

                                                                                                                                                  typewind=[snacksname,
                                                                                                                                                                            snacksprice,
                                                                                                                                                                            chatbutton
                                                                                                                                                                            [sg.B("BACK")]]
                                                                                                                                                  mad,vals=sg.Window(" ",typewind,default_button_element_size=(3,1), auto_size_buttons=False)
                                                                                                                                                  typewind.read()
                                                                                                                                                  typewind.close()
                                                                                        
                                                                                                                                                  if mad=="BACK" or sg.WIN_CLOSED:
                                                                                                                                                                          maalu=maalu-1
                                                                                                                                                  for thor in refreshments.index:
                                                                                                                                                                          if mad==refreshments.loc[thor]["item"]:
                                                                                                                                                                                  sg.popup("1 item added")
                                                                                                                                                                                  orderedsnacksname.append(mad)
                                                                                                                                                                                  orderedsnacksprice.append(int(refreshments.loc[thor]["cost"]))
                                                                                                                                                                                  
                                                                                                                                                                                  
                                                                                                                                                        
                                                                                                                                                  if item=="NEXT":
                                                                                                                                                          print("sucess")
                                                                                                                                                          
                                                                                                                                                                     
                                                                                                                                          sunny=sunny+1                        
                                                                                                                                                          











                                                                                                                                                                                                                                                        
