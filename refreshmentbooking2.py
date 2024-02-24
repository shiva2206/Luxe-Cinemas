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


orderedsnacksname=[]
orderedsnacksprice=[]
orderedsnacksquantity=[] 
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
                                                                                                                                               textsnackstype.append(sg.T(uniquesnackstype[tip],size=(29,1),justification="c"))
                                                                                                                                               imagesnacksimage.append(sg.Image(uniquesnacksimage[tip]))
                                                                                                                                               snacksbutton.append(sg.B("ORDER",key=uniquesnackstype[tip]))
                                                                                                                                                                                                                                      

     
                                                                                                                                                                   
                                                                                                                                         
                                                                                                                                                  
                                                                                                                                          print("to")                                                                                         
                                                                                                                                          snackswindow=[[sg.T("R E F R E S H M E N T S",size=(90,1),font=("arial",15),justification='c')],
                                                                                                                                                                textsnackstype,
                                                                                                                                                                imagesnacksimage,
                                                                                                                                                                snacksbutton,
                                                                                                                                                               [sg.B("NEXT"),sg.B("PREVIOUS")] ]                   
                                                                                                                                          dora=sg.Window(" k",snackswindow,default_button_element_size=(29,1), auto_size_buttons=False)                           
                                                                                                                                          item,vals=dora.read()                                                                                          
                                                                                                                                          dora.close()

                                                                                                                                          snacksname=[]
                                                                                                                                                  
                                                                                                                                          snacksprice=[]
                                                                                                                                          chatbutton=[]
                                                                                                                                          refreshmentsname=[]
                                                                                                                                          refreshmentsprice=[]
                                                                                                                                          refreshmentlisting=[]
                                                                                                                                  

                                                                                                                                                  

                                                                                                                                                  
                                                                                                                                          for yoyo in uniquesnackstype:                                          
                                                                                                                                                          if item==yoyo:
                                                                                                                                                        
                                                                                                                                                                  refreshments=refreshments[refreshments.type==item]
                                                                                                                                                                  refreshmentlisting.append([sg.T(yoyo,size=(15,1),font=("arial",20),justification='c')])
                                                                                                                                                                  for jog in refreshments.index:                                                                               
                                                                                                                                                                          snacksname.append(sg.T(refreshments.loc[jog]["item"],size=(15,1)))
                                                                                                                                                                          snacksprice.append(sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(15,1)))           
                                                                                                                                                                          chatbutton.append(sg.B("ADD",key=refreshments.loc[jog]["item"]))
                                                                                                                                                                          refreshmentsname.append(refreshments.loc[jog]["item"])
                                                                                                                                                                          refreshmentsprice.append(refreshments.loc[jog]["cost"])
                                                                                                                                                                          
                                                                                                                                                                          refreshmentlisting.append([sg.T(refreshments.loc[jog]["item"],size=(15,1)),sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(15,1)),sg.B("ADD",key=refreshments.loc[jog]["item"])])
                                                                                                                                                                  refreshmentlisting.append([sg.B("BACK")])        

                                                                                                                                                                  typ=refreshmentlisting                                                                      
                                                                                                                                                                            
                                                                                                                                                                  typewind=sg.Window(" ",typ,default_button_element_size=(14,1), auto_size_buttons=False)
                                                                                                                                                                  mad,vals=typewind.read()

                                                                                                                                                  
                                                                                                                                                                  typewind.close()
                                                                                        
                                                                                                                                                                  if mad=="BACK" or mad==sg.WIN_CLOSED:
                                                                                                                                                                          sunny=sunny-1
                                                                                                                                                                        
                                                                                                                                                                  for thor in range(len(refreshmentsname)):
                                                                                                                                                                          if mad==refreshmentsname[thor]:
                                                                                                                                                                                  sg.popup(mad,"1 item added")
                                                                                                                                                                                  orderedsnacksname.append(mad)
                                                                                                                                                                                  orderedsnacksprice.append(int(refreshmentsprice[thor]))
                                                                                                                                                                                  sunny=sunny-1
                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                  
                                                                                                                                                                                  
                                                                                                                                                        
                                                                                                                                          if item=="NEXT":
                                                                                                                                                  rice=0
                                                                                                                                                  while rice<1:
                                                                                                                                                                     finalrefreshmentlisting=[]

                                                                                                                                                                     if len(orderedsnacksname)!=0:
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("click to delete item",size=(45,1),justification='r')])
                                                                                                                                                                     
                                                                                                                                                                                     for kar in range(len(orderedsnacksname)):
                                                                                                                                                                                             finalrefreshmentlisting.append(([sg.T(orderedsnacksname[kar],size=(15,1)),sg.T(orderedsnacksprice[kar],size=(15,1)),sg.B(orderedsnacksname[kar])]))
                                                                                                                                                                     
                                                                                                                                                        

                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("Total cost",size=(15,1)),sg.T("Rs:"+str(sum(orderedsnacksprice)),size=(15,1))])
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("total quantity = "+str(len(orderedsnacksprice)))])
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.B("Back"),sg.B("proceed"),sg.B("delete all")])
                                                                                                                                                                     else:
                                                                                                                                                                                    finalrefreshmentlisting.append([sg.B("proceed"),sg.B("Back")])
                                                                                                                                                                                             

                                                                                                                                                                     lake=finalrefreshmentlisting
                                                                                                                                                                     corn=sg.Window("final",lake,default_button_element_size=(14,1), auto_size_buttons=False)
                                                                                                                                                                     bad,vals=corn.read()
                                                                                                                                                                     corn.close()
                                                                                                                                                                     if (bad=="Back" or bad==sg.WIN_CLOSED)  :
                                                                                                                                                                  
                                                                                                                                                                            rice=rice
                                                                                                                                                                            sunny=sunny-1
                                                                                                                                                                  
                                                                                                                                                                          
                                                                                                                                                                        
                                                                                                                                                                     elif bad!="proceed" and bad!="delete all":
                                                                                                                                                                           print("hi")
                                                                                                                                                                           orderedsnacksprice.remove(orderedsnacksprice[orderedsnacksname.index(bad)])
                                                                                                                                                                           orderedsnacksname.remove(bad)
                                                                                                                                                                  
                                                                                                                                                                           rice=rice-1
                                                                                                                                                                     if bad=="proceed":
                                                                                                                                                                             print("succeded")
                                                                                                                                                                             
                                                                                                                                                                     elif bad=="delete all":
                                                                                                                                                                             orderedsnacksname=[]
                                                                                                                                                                             orderedsnacksprice=[]
                                                                                                                                                                             sunny=sunny-1
                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                     rice=rice+1                                                                                   
                                                                                                                            
                                                                                                                                                                  
                                                                                                                                                              
                                                                                                                                                          
                                                                                                                                                         
                                                                                                                                                        
                                                                                                                                                  
                                                                                                                                          if item=="PREVIOUS":                                                                     
                                                                                                                                                     print("condtruction")
                                                                                                                                                     orderedsnacksname=[]
                                                                                                                                                     orderedsnacksprice=[]
                                                                                                                                                     orderedsnacksquantity=[] 
                                                                                                                                          sunny=sunny+1
                                                                                                                                          
                                                                                                                                                          











                                                                                                                                                                                                                                                        
