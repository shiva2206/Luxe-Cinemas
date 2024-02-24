import PySimpleGUI as sg
import pandas as pd
import datetime
import random as rd
from datetime import datetime
import datetime as dt
def unique_value(dataframe,column):
    lt=[]
    for var in dataframe[column]:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)
def uniquelist(dataframe):
    lt=[]
    for var in dataframe:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)



orderedsnacksname=[]
orderedsnacksprice=[]
                                                                                                      
sunny=0
bill=0
while sunny<1:                                                                                                    
                                                                                                                                          refreshments=pd.read_csv("movie refreshments.csv")                                                                                
                                                                                                                                          refreshments=refreshments.set_index("id")
                                                                                                                                          
                                                                                                                                          uniquesnackstype=unique_value(refreshments,"type")                                               
                                                                                                                                          uniquesnacksimage=unique_value(refreshments,"image")                                 
                                                                                                                                          
                                                                                                                                          textsnackstype=[]                                                                          
                                                                                                                                          imagesnacksimage=[]
                                                                                                                                          snacksbutton=[]                                                                          
                                                                                                                                          for tip in range(len(uniquesnackstype)):
                                                                                                                                               textsnackstype.append(sg.T(uniquesnackstype[tip].upper(),size=(27,1),font=("arial",13),justification="c"))
                                                                                                                                               imagesnacksimage.append(sg.Image(uniquesnacksimage[tip]))
                                                                                                                                               snacksbutton.append(sg.B("ORDER NOW",key=uniquesnackstype[tip]))
                                                                                                                                                                                                                                      

     
                                                                                                                                                                   
                                                                                                                                         
                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                          snackswindow=[[sg.T("R E F R E S H M E N T S",size=(31,1),font=("Times",40),justification='c')],
                                                                                                                                                                textsnackstype,                                                                       
                                                                                                                                                                imagesnacksimage,
                                                                                                                                                                snacksbutton,
                                                                                                                                                               [sg.B("PREVIOUS",size=(60,1)),sg.B("NEXT",size=(60,1))] ]                   
                                                                                                                                          dora=sg.Window(" ",snackswindow,default_button_element_size=(29,1), auto_size_buttons=False)                                          
                                                                                                                                          item,vals=dora.read()                                                                                          
                                                                                                                                          dora.close()
                                                                                                                                          blesso=0
                                                                                                                                          while blesso<1:

                                                                                                                                                  snacksname=[]
                                                                                                                                                  
                                                                                                                                                  snacksprice=[]                                                                               
                                                                                                                                                  chatbutton=[]
                                                                                                                                                  refreshmentsname=[]
                                                                                                                                                  refreshmentsprice=[]
                                                                                                                                                  refreshmentlisting=[]                                                                                                                               
                                                                                                                                  

                                                                                                                                                  

                                                                                                                                         
                                                                                                                                                  for yoyo in uniquesnackstype:                                          
                                                                                                                                                          if item==yoyo:
                                                                                                                                                        
                                                                                                                                                                  refreshments=refreshments[refreshments.type==item]                                                                  
                                                                                                                                                                  refreshmentlisting.append([sg.T(yoyo.upper(),size=(30,1),font=("arial",20),justification='c')])
                                                                                                                                                                  refreshmentlisting.append([sg.T("Item Name",size=(8,1),font=("Times",17)),sg.T("cost",size=(8,1),font=("Times",17),justification='c'),sg.T("          click to add",size=(15,1),font=("Times",17),justification='c')])
                                                                                                                                                                  for jog in refreshments.index:                                                                               
                                                                                                                                                                          snacksname.append(sg.T(refreshments.loc[jog]["item"],size=(15,1)))
                                                                                                                                                                          snacksprice.append(sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(15,1)))           
                                                                                                                                                                          chatbutton.append(sg.B(refreshments.loc[jog]["item"]))
                                                                                                                                                                          refreshmentsname.append(refreshments.loc[jog]["item"])
                                                                                                                                                                          refreshmentsprice.append(refreshments.loc[jog]["cost"])
                                                                                                                                                                          
                                                                                                                                                                          refreshmentlisting.append([sg.T(refreshments.loc[jog]["item"],size=(20,1)),sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(20,1)),sg.B("ADD",key=refreshments.loc[jog]["item"])])
                                                                                                                                                                  refreshmentlisting.append([sg.B("BACK")])                                                                                            

                                                                                                                                                                  typ=refreshmentlisting
                                                                                                                                                                            
                                                                                                                                                                  typewind=sg.Window(" ",typ,default_button_element_size=(14,1), auto_size_buttons=False)  
                                                                                                                                                                  mad,vals=typewind.read()

                                                                                                                                                  
                                                                                                                                                                  typewind.close()                                                                  
                                                                                        
                                                                                                                                                                  if mad=="BACK" or mad==sg.WIN_CLOSED:
                                                                                                                                                                          sunny=sunny-1
                                                                                                                                                                        
                                                                                                                                                                  for thor in range(len(refreshmentsname)):
                                                                                                                                                                          if mad==refreshmentsname[thor]:
                                                                                                                                                                                  sg.popup(mad,"+1 Item Added")                                                                                                                                                                                                        
                                                                                                                                                                                  orderedsnacksname.append(mad)
                                                                                                                                                                                  orderedsnacksprice.append(int(refreshmentsprice[thor]))
                                                                                                                                                                                  blesso=blesso-1
                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                  blesso=blesso+1                                
                                                                                                                                                                                  
                                                                                                                                                        
                                                                                                                                          if item=="NEXT":
                                                                                                                                                  
                                                                                                                                                      
                                                                                                                                                  rice=0
                                                                                                                                                  bill=0
                                                                                                                                                  while rice<1:
                                                                                                                                                                  
                                                                                                                                                                     
                                                                                                                                                                     orderedsnacksquantity=[]
                                                                                                                                                                     uniqueorderedsnacksname=uniquelist(orderedsnacksname)                                                          
                                                                                                                                                                     uniqueorderedsnacksprice=uniquelist(orderedsnacksprice)
                                                                                                                                                                     
                                                                                                                                                                     print("uniqueorderedsnacksname:",uniqueorderedsnacksname)
                                                                                                                                                                     print("uniqueorderedsnacksprice:",uniqueorderedsnacksprice)
                                                                                                                                                                     for wiz in uniqueorderedsnacksname:
                                                                                                                                                                          quan=0
                                                                                                                                                                          for electro in orderedsnacksname:
                                                                                                                                                                              if wiz==electro:
                                                                                                                                                                                  quan=quan+1
                                                                                                                                                                          orderedsnacksquantity.append(quan)
                                                                                                                                                                     print("orderedsnacksquantity",orderedsnacksquantity)     
                                                                                                                                                                              
                                                                                                                                                                     finalrefreshmentlisting=[]

                                                                                                                                                                     if len(orderedsnacksname)!=0:
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("SNACKS BILL",size=(30,1),font=("times",20),justification='c')])
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("Items     cost       quantity     click to delete(-1)",size=(45,1),font=("arial",15),justification='c')])
                                                                                                                                                                     
                                                                                                                                                                                     for kar in range(len(uniqueorderedsnacksname)):
                                                                                                                                                                                             finalrefreshmentlisting.append(([sg.T(uniqueorderedsnacksname[kar],size=(15,1)),sg.T(orderedsnacksprice[kar],size=(15,1)),sg.T(orderedsnacksquantity[kar],size=(5,1)),sg.B("REMOVE",key=uniqueorderedsnacksname[kar])]))

                                                                                                                                                                                        
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])                                              

                                                                                                                                                                                     finalrefreshmentlisting.append([sg.T("Total cost",size=(15,1)),sg.T("Rs:"+str(sum(orderedsnacksprice)),size=(15,1)),sg.T("Total quantity = "+str(len(orderedsnacksprice)),size=(15,1),justification='l')])
                                                                                                                                                                                     
                                                                                                                                                                                     finalrefreshmentlisting.append([sg.B("Back"),sg.B("Proceed"),sg.B("Delete All")])
                                                                                                                                                                     else:
                                                                                                                                                                                    finalrefreshmentlisting.append([sg.B("Proceed",size=(20,1)),sg.B("Back",size=(20,1))])
                                                                                                                                                                                             

                                                                                                                                                                     lake=finalrefreshmentlisting                                    
                                                                                                                                                                     corn=sg.Window("Refreshment Bill",lake,default_button_element_size=(14,1), auto_size_buttons=False)
                                                                                                                                                                     bad,vals=corn.read()                                                       
                                                                                                                                                                     corn.close()
                                                                                                                                                                     if (bad=="Back" or bad==sg.WIN_CLOSED)  :                                              
                                                                                                                                                                  
                                                                                                                                                                            rice=rice
                                                                                                                                                                            sunny=sunny-1
                                                                                                                                                                  
                                                                                                                                                                          
                                                                                                                                                                        
                                                                                                                                                                     elif bad!="Proceed" and bad!="Delete All":
                                                                                                                                                                           
                                                                                                                                                                           bat=0
                                                                                                                                                                           iq=-1
                                                                                                                                                                           print("bad:",bad)  
                                                                                                                                                                           for god in range(len(orderedsnacksname)):
                                                                                                                                                                                
                                                                                                                                                                                if orderedsnacksname[god]==bad :
                                                                                                                                                                                    bat=bat+1                                                                                
                                                                                                                                                                                    
                                                                                                                                                                                    for monk in range(len(uniqueorderedsnacksname)):
                                                                                                                                                                                        if bad==uniqueorderedsnacksname[monk]:
                                                                                                                                                                                            iq=orderedsnacksquantity[monk]
                                                                                    
                                                                                                                                                                                            ram=monk
                                                                                                                                                                                       
                                                                                                                                                                                    print("bat",bat)      
                                                                                                                                                                                    if bat==iq:                                                                     
                                                                                                                                                                                         
                                                                                                                                                                                         sai=god
                                                                                                                                                                                         finish=1
                                                                                                                                                                                         print("finish",finish)
                                                                                                                                                                                         
                                                                                                                                                                           if finish==1:
                                                                                                                                                                                

                                                                                                                                                                                del(orderedsnacksprice[sai])
                                                                                                                                                                                
                                                                                                                                                                                del(orderedsnacksname[sai])
                                                                                                                                                                                del(orderedsnacksquantity[ram])
                                                                                                                                                                                    
                                                                                                                                                                  
                                                                                                                                                                           rice=rice-1
                                                                                                                                                                     if bad=="Proceed":
                                                                                                                                                                         
                                                                                                                                                                         now=dt.datetime.now()
                                                                                                                                                                         nowstr=now.strftime("%d/%m/%Y %H:%M:%S")
                                                                                                                                                                         today,time=nowstr.split(' ')
                                                                                                                                                                         todayday,todaymonth,todayyear=today.split('/')
                                                                                                                                                                         if todayday[0]=="0":
                                                                                                                                                                             todayday=todayday.replace("0","")
                                                                                                                                                                         if todaymonth[0]=="0":
                                                                                                                                                                             todaymonth=todaymonth.replace("0","")
                                                                                                                                                                         today=todayday+"/"+todaymonth+"/"+todayyear    
                                                                                                                                                                         offlinecustomersnacks=pd.read_csv("offlinecustomer snacks.csv")
                                                                                                                                                                         offlinecustomersnacks=offlinecustomersnacks.set_index("_")
                                                                                                                                                                         for you in range(len(orderedsnacksname)):
                                                                                                                                                                                        kasx=refreshments[refreshments.item== orderedsnacksname[you]]   
                                                                                                                                                                                        offlinecustomersnacks.loc[max(offlinecustomersnacks.index)+1]=today,orderedsnacksname[you],kasx.loc[max(kasx.index)]["type"],str(1),orderedsnacksprice[you]

                                                                                                                                                                         offlinecustomersnacks.to_csv("offlinecustomer snacks.csv")                                                                                                                        
                                                                                                                                                                     elif bad=="Delete All":
                                                                                                                                                                             orderedsnacksname=[]
                                                                                                                                                                             orderedsnacksprice=[]
                                                                                                                                                                             orderedsnacksquantity=[]
                                                                                                                                                                             sunny=sunny-1
                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                     rice=rice+1                                                                                                             
                                                                                                                                                                     
                                                                                                                            
                                                                                                                                          sunny=sunny+1        
