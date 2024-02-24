import PySimpleGUI as sg
import pandas as pd
u=0



while u<1:

                                                                     noseatslist=[1,2,3,4,5,6,7,8,9,10]
                                                                     layout=[[sg.T("no of seats to book")],
                                                                                                        [sg.B("1"),sg.B("2"),sg.B("3"),sg.B("4"),sg.B("5"),sg.B("6"),sg.B("7"),sg.B("8"),sg.B("9"),sg.B("10")],
                                                                                                        [sg.B('back')]]
                                                                     window=sg.Window("noseats",layout,default_button_element_size=(3,1), auto_size_buttons=False)
                                                                     gym,vals = window.read()
                                                                     window.close()
                                                                     i=0 
                                                                     if gym==sg.WIN_CLOSED or gym=='back' :
                                                                                 print('hi')
                                                                                 
                                                                                
                                        
                                                                                 
                                                                                                                          
     
     
                                                                     else:
                                                                             for ps in noseatslist:
                                                                                                                          if gym==str(ps):
                                                                                                                                noseats=ps
                                                                                                                               
                                                                             p=0

                                                                             seatrow=[]
                                                                             seatno=[]
                                                                             index=[]
                                                                             silverseats=[]
                                                                             premiereseats=[]
                                                                             
                                                                             while i<=noseats:
                                                                                    

                                                                                     print("file:")
                                                                                     a=pd.read_csv("Fseat1.csv")
                                                                                     a=a.set_index("_")
                                                                                     


                                                                                     
                                                                                     kkk=[]
                                                                                     jjj=[]
                                                                                     iii=[]
                                                                                     hhh=[]
                                                                                     ggg=[]
                                                                                     fff=[]
                                                                                     eee=[]
                                                                                     ddd=[]
                                                                                     ccc=[]
                                                                                     bbb=[]
                                                                                     aaa=[]
                                                                                     rows=[kkk,jjj,iii,hhh,ggg,fff,eee,ddd,ccc,bbb,aaa]                                                                                  
 
                                                                                     for var in a.index:
                                                                                           for dor in range(1,11):
                                                                                                 if a.loc[var][str(dor)]=="BKED":
                                                                                                        rows[var].append(sg.T("BKED"))
                                                                                                 elif a.loc[var][str(dor)]==" THIS ":
                                                                                                        rows[var].append(sg.T(" THIS "))    
                                                                                                 else:
                                                                                                        rows[int(var)].append(sg.B(a.loc[int(var)][str(dor)]))                                                  
 
                                                                                     for sumo in rows: 
                                                                                                sumo.insert(-2,sg.T("|   |"))
                                                                                                sumo.insert(2,sg.T("|   |"))
                                                                                                
                                                                                                sumo.insert(0,sg.T("|   |"))
                                                                                                sumo.append(sg.T("|   |"))  
                                                                                     alphabets=["K","J","I","H","G","F","E","D","C","B","A"]     
                                                                                     if i==noseats and i==len(seatno) :

         
                                                                                                butt=sg.B("BOOK")
                                                                                            

                                                                                     else:
                                                                                                butt=sg.T("")
                                                                                     back=sg.B("back")
                                                                                     

                                                                                     if i<=noseats:
                                                                                                lay=[[sg.T("SOAPANASUNDARI - 1",size=(55,1),justification='c',font=("arial",15))],
                                                                                                    [sg.T("EXT"),sg.T("                                                                                                                                "),sg.T("EXT")],
                                                                                                      kkk,
                                                                                                       jjj,
                                                                                                     [sg.T("|   |___  ___  ___  ___  ___  ___  ___  __  __  __   ___   ___   ___  ___   ___   ___  ___   ___ |   |")],
                                                                                                     iii,
                                                                                                     hhh,
                                                                                                     ggg,
                                                                                                     fff,
                                                                                                     eee,
                                                                                                     ddd,
                                                                                                     ccc,
                                                                                                     bbb,
                                                                                                     aaa,
                                                                                                     [sg.T("|   |___  ___  ___  ___  ___  ___  ___  __  __  __   ___   ___   ___  ___   ___   ___  ___   ___ |  |")],
                                                                                                                 [sg.T("____________________________________________________________________________________")],
                                                                                                    [sg.T("                     A  L  L         E  Y  E  S        T  H  I  S        W  A  Y         P  L  E  A  S  E               ")],
                                                                                                   [sg.T("____________________________________________________________________________________") ],
                                                                                                  [butt,back,sg.T("BKED  - already booked"),sg.T("               THIS   -  seat selected by you")],
                                                                                                  [sg.T("                           "),sg.T("SILVER(A-I): Rs 150",font=("arial",10)),sg.T("    "),sg.T("PREMIERE(J,K): Rs 170",font=("arial",10)),sg.T("   seats left for selection :"+str(noseats-i)+" ")]]
                                                                                                window=sg.Window("bookingscreen",lay,default_button_element_size=(4,1), auto_size_buttons=False)
                                                                                                bucket,vals = window.read()
                                                                                                window.close()
                                                                                     print("i","noseats",i,noseats)           
                                                                                     if  i<noseats :
                                                                                             for dum in a.index:
                                                                                                     for col in range(1,11):
                                                                                                              if bucket== a.loc[dum][str(col)]:
                                                                                                                      for gg in range(len(a.loc[dum][str(col)])):                                                                                  
                                                                                                                                    print(bucket,a.loc[dum][str(col)])
                                                                                                                                    if gg==0:
                                                                                                                                              seatrow.append((a.loc[dum][str(col)])[0])
                                                                                                                                              print(seatrow)                                                                                                            
                                                                                                                                              
                                                                                                                      seatno.append(str(col))
                                                                                                                      print("seatno.append(str(col))",str(col))
                              
                                                                                                                      a.loc[dum][str(col)]=" THIS "
                                                                                                                      index.append(dum)
                                                                                                                      a.to_csv("Fseat1.csv")
                                                                                                                      
                                                                                                                      print("boked")
                                                                                                                      i=i+1
                                                                                     if bucket=="back" and len(seatno)!=0:
                                                                                             i=i-1
                                                                                             a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                             print(" event==+back+ and len(seatno)!=0")
                                                                                             del(seatrow[-1])
                                                                                             del(seatno[-1])
                                                                                             del(index[-1])
                                                                                             
                                                                        
                                                                                            
                                                                                             a.to_csv("Fseat1.csv")
                                                                                     elif bucket==sg.WIN_CLOSED :

                                                                                             if len(seatno)!=0:
                                                                                                   i=0
                                                                                                   for k in range(len(seatno)):
                                                                                                 
                                                                                                     
                                                                                                        a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                                        print("this==1 and event==+back+ and len(seatno)!=0")
                                                                                                        del(seatrow[-1])
                                                                                                        del(seatno[-1])
                                                                                                        del(index[-1])
                                                                                             else:
                                                                                                   i=1+noseats
                                                                                                   u=u-1
                                                                        
                                                                                             
                                                                                             a.to_csv("Fseat1.csv")
                                                                                             silverseats=[]
                                                                                             premiereseats=[]
                                                                                             
                                                                                            

                                                                                     elif bucket=="back" and len(seatno)==0:
                                                                                              print("bucket==back and len(seatno)")
                                                                                              u=u-1
                                                                                              i=noseats+1


                                                                                             
                                                                                     if  bucket=="BOOK":
                                                                                             i=noseats+1
                                                                                             
                                                                                             for hi in range(len(seatrow)):
                                                                                                             if seatrow[hi]=="J" or seatrow[hi]=="K":
                                                                                                                 premiereseats.append((seatrow[hi],seatno[hi]))
                                                                                                             else:
                                                                                                                 silverseats.append((seatrow[hi],seatno[hi]))
                                                                                     
                                                                     u=u+1
