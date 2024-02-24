import PySimpleGUI as sg
import pandas as pd
import datetime
import random as rd
from pygame import mixer
from datetime import datetime
import datetime as dt
customer=pd.read_csv("customer.csv")
customersnacks=pd.read_csv("customer snacks.csv")
ww=0
while ww<1:
            num=[[sg.Text("enter your name")],[sg.Input()],
                 [sg.T("enter your phone number")],[sg.Input()],
                 [sg.T("enter your codeno")],[sg.Input()],
                 [sg.B("submit"),sg.B("back")]]

            tata=sg.Window("number",num)
            ting,vals=tata.read()
            tata.close()
            
            looty=0
            if ting=="submit":
                  number=(vals[1])
                  customername=vals[0]
                  codeno=vals[2]
                  codeno=int(codeno)
                  number=str(number)
                  if len(number)!=10  :
                         sg.popup("enter valid number")
                         ww=ww-1
                  else:
                       pain=0
                       while pain<1:
                            ktm=0
                            for guc in range(len(customer.values)): 
                                 if customer.values[guc][0]==customername and  str(customer.values[guc][1])==number and  customer.values[guc][2]==codeno and ktm==0:
                                      looty=1
                                      ktm=1
                                     
                                      customerdetails=customer[customer.codenos==codeno]
                                      bookingscreenloc=unique_value(customerdetails,"bookingscreen")
                                      customerdetails=customerdetails.drop(["name","phnno","codenos","programtime","bookingscreen"],axis=1)
                                      customersnacksdetails=customersnacks[customersnacks.codenos==codeno]
                                      customersnacksdetails=customersnacksdetails.drop(["name","phnno","codenos"],axis=1)
                                      a=pd.read_csv("Fseat5.csv")
                                                    
                                      a=a.set_index("alphabets")
                                      totaltickets=len(customerdetails)
                                      if len(customersnacksdetails)==0:
                                                    sg.popup("name:"+customername+"   "+"phnno:"+number+"   "+"codenos:"+str(codeno),customerdetails,"totaltickets:"+str(totaltickets),title="details")
                                            
                                      else:
                                                    sg.popup("name:"+customername+"   "+"phnno:"+number+"   "+"codenos:"+str(codeno),customerdetails,"totaltickets:"+str(totaltickets),"SNACKS DETAILS  ",customersnacksdetails,"quantity:"+str(len(customersnacksdetails)),title="details")
                                 
                                      if eventing!='MY DETAILS':
                                            customerdetails=customer[customer.codenos==codeno]
                                            customerdetails=customerdetails.drop(["name","phnno","codenos","bookingscreen"],axis=1)


                                          
                                            now=dt.datetime.now()
                                            for t in customerdetails.index:
                                                print("")
                                            timeobj=customerdetails.loc[t]['date']+(" ")+customerdetails.loc[t]['programtime']
                                            timeformat=datetime.strptime(timeobj,"%d/%m/%Y %H:%M")-dt.timedelta(minutes=30)
                                            if timeformat<now:
                                                sg.popup("you cant cancel since time is up")
                                            else:
                                                customerdetailslist=[[sg.T("tick to cancel")],[sg.T(" ",size=(10,1)),sg.T("seat alp",size=(10,1)),sg.T("seat no",size=(10,1))]]
                                                cusindex=list(customerdetails.index)
                                                cusseatalp=list(customerdetails.seat)
                                                cusseatno=list(customerdetails.no)
                                                cusseatalpno=[]
                                                indexdel=[]
                                                for pro in range(len(cusindex)):
                                                    customerdetailslist.append([sg.T(str((pro+1)),size=(10,1)),sg.T(cusseatalp[pro],size=(10,1)),sg.T(str(cusseatno[pro]),size=(10,1)),sg.Checkbox("remove",key=cusseatalp[pro]+str(cusseatno[pro]),size=(10,1))])
                                                    cusseatalpno.append(cusseatalp[pro]+str(cusseatno[pro]))
                                                customerdetailslist.append([sg.B("OK")])    
                                                icewiz=customerdetailslist
                                                punk=sg.Window("cancellation",icewiz)
                                                dumal,vals=punk.read()
                                                punk.close()
                                                if dumal==sg.WIN_CLOSED:
                                                    print("")
                                                elif dumal=="OK":
                                                    cashreturn=0
                                                   
                                                    for maxi in range(len(cusseatalpno)):
                                                         if vals[cusseatalpno[maxi]]==True:
                                                              customer.drop([maxi])
                                                              
                                                              cashreturn=cashreturn+customerdetails.loc[cusindex[maxi]]["cost"]
                                                              a.loc[cusseatalp[maxi]][cusseatno[maxi]]=cusseatalpno[maxi]
                                                    a.to_csv("Fseat5.csv")
                                                    customer.to_csv("customer.csv")
                                                    customerdetails=customer[customer.codenos==int(codeno)]
                                                    if len(customerdetails)==1:
                                                         customersnacks.drop(customersnacksdetails.index)
                                                         customersnacks.to_csv("customer snacks.csv")
                                                              
                                                    sg.popup("scucessfully cancelled and cash Rs:"+str(cashreturn)+"retured")          
    
                                            
                                      vari=vari-1    
                            pain=pain+1          
    
                       if looty==0:
                              sg.popup("your mobileno or codeno or name is invalid") 
                              ww=ww-1
