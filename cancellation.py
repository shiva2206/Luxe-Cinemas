import PySimpleGUI as sg
import pandas as pd

customer=pd.read_csv("customer.csv")
customer=customer.set_index("_")
customersnacks=pd.read_csv("customer snacks.csv")
customersnacks=customersnacks.set_index("_")

      ww=0
      while ww<1:
            num=[[sg.Text("enter your name")],[sg.Input()],
                 [sg.T("enter your phone number")],[sg.Input()],
                 [sg.T("enter your codeno")],[sg.Input()],
                 

                 [sg.B("submit"),sg.B("back")]]

            tata=sg.Window("number",num)
            ting,vals=tata.read()
            tata.close()
            number=(vals[1])
            customername=vals[0]
            codeno=vals[2]
            looty=0

            if ting=="submit":
                  number=str(number)
                  
                  if len(number)!=10  :
                         sg.popup("enter valid number")
                         ww=ww-1
                  else:
                       pain=0
                       while pain<1:
                            ktm=0
                            for guc in range(len(customer.values)):
                                 
                                 if customer.values[guc][0]==customername and  str(customer.values[guc][1])==number and  str(customer.values[guc][2])==codeno and ktm==0:
                                      looty=1
                                      ktm=1
                                      customerdetails=customer[customer.codenos==codeno]
                                      customersnacksdetails=customersnacks[customersnacks.codenos==codeno]
                                      if eventing=='MY DETAILS': 
                                            sg.popup(customerdetails)
                                            
                                      else:
                                          sg.popup("under construction")
                                      vari=vari-1    
                            pain=pain+1          




                           
                       if looty==0:

                              sg.popup("your mobileno or codeno or name is invalid")
                              
                              ww=ww-1
                              
                              
                                    
                         
              

            elif ting==sg.WIN_CLOSED :
                
                  
            ww=ww+1       
