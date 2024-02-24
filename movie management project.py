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





csvloc=["Fseat1.csv","Fseat2.csv","Fseat3.csv","Fseat4.csv","Fseat5.csv","Fseat6.csv","Sseat1.csv","Sseat2.csv","Sseat3.csv","Sseat4.csv","Sseat5.csv","Sseat6.csv","SUseat1.csv","SUseat2.csv","SUseat3.csv","SUseat4.csv","SUseat5.csv","SUseat6.csv"]





vari=0
while vari<1:
  layout0=[
                [sg.Image('welcome image.png')],
                [sg.Button('BOOK TICKETS',size=(27,1)),sg.Button('MY DETAILS',size=(27,1)),sg.Button('CANCEL TICKETS',size=(27,1))],
                [                                                                         sg.Button('EXIT',size=(86,1))                                                                                            ]
                ]
  window0=sg.Window('SOAPANASUNDARI CINEMAS',layout0)
  variable0=0
  eventing,values=window0.read()
  while variable0<1:
      
      onetimeselect=0
      multitime=0
      if eventing=='BOOK TICKETS':
          variable1=0
          while variable1<1:
                df=pd.read_csv('movie timing pro.csv')
                df=df.set_index('_')
            
                            
                uniquedate=unique_value(df,'date')
                uniquemoviename=unique_value(df,'movie')
                uniquemovieimage=unique_value(df,'image file 1')
                uniquemovieimage2=unique_value(df,'image file 2')
                lst=[]
                onetimeselect=1+onetimeselect
                if onetimeselect==1:
                              lst.append(sg.T(uniquedate[0],size=(40,1),justification='center'))
                              showdate=uniquedate[0]
                              showdatemovies=[]
                              uniqueshowdatemovies=[]
                              uniqueimages=[]
                              showdatetime=[]
                              for kg in (df[df.date==uniquedate[0]]).values:
                                     showdatemovies.append(kg[2])
                                     showdatetime.append(kg[4])
                              uniqueshowdatemovies=unique_value(df[df.date==uniquedate[0]],'movie')
            
                              uniqueimages=unique_value(df[df.date==uniquedate[0]],'image file 1')
                              uniqueimages2=unique_value(df[df.date==uniquedate[0]],'image file 2')
                              
                              uniquedate.remove(uniquedate[0])
                              for wwe in uniquedate:
                                     lst.append(sg.B(wwe,size=(40,1)))
                else:
                       for wwe in uniquedate:
                            if event!=wwe :
                                     lst.append(sg.B(wwe,size=(40,1)))
                            elif event==wwe or showdate==wwe:
                                     lst.insert(uniquedate.index(wwe),sg.T(wwe,size=(40,1),justification='center'))
                                     showdate=wwe
                                     showdatemovies=[]
                                     uniqueshowdatemovies=[]
                                     uniqueimages=[]
                                     showdatetime=[]
                                     for kg in (df[df.date==wwe]).values:
                                             showdatemovies.append(kg[2])
                                             showdatetime.append(kg[4])
                                     uniqueshowdatemovies=unique_value(df[df.date==wwe],'movie')
                                     uniqueimages=unique_value(df[df.date==wwe],'image file 1')
                bookingimage=[]
                bookingbutton=[]
                for dj in range(len(uniqueimages)):
                                     bookingimage.append(sg.Image(filename=uniqueimages[dj]) )
                                     bookingbutton.append(sg.B(uniqueshowdatemovies[dj],size=(29,1)))
            
                window0.close()    
                layout1=[lst,
                                         [sg.T(' ')],
                                         [sg.T('---------------------------------------------------------------------------Showing On '+showdate+'------------------------------------------------------------------------------------',justification='center',size=(124,1))],
                                         [sg.T('-------------- B  O  O  K        N  O  W --------------',size=(len(uniqueshowdatemovies)*22,1),font=('arial',15),justification='c')],
                                          bookingimage,
                                           bookingbutton,
                                         [sg.T(' ')],
                                          [sg.Button('BACK',size=(124,1))],
                                          [sg.T(' ')]
                                                     ]
                window1=sg.Window('Showing Today',layout1)
                event,values=window1.read()
                window1.close()
                if event=='BACK' or event==sg.WIN_CLOSED:
                                     variable1=variable1+1
                                     
                                     variable0=variable0+1
                                     vari=vari-1
                                     event=showdate
                timebutton=[]
                imagebutton=[]

                directedby=[sg.T('directed by:')]
                cast=[sg.T('cast:')]
                genre=[sg.T('genre:')]
                
                
                
                
                for buti in uniqueshowdatemovies:
                    if event==buti:
                        sandy=0
                        while sandy<1:
                                  imagebutton.append(sg.Image(df.loc[(df.loc[(df[df.movie==buti]).index]['image file 2']).index[0]]['image file 2']))
                                  indexnum=0
                                  for kuti in range(len(showdatemovies)):
                                         if showdatemovies[kuti]==buti:
                                                indexnum=indexnum+1
                                                timebutton.append(sg.B(showdatetime[kuti],size=(7,1)))
                                  toein=0
                                  for bravo in range(len(df)):
                                         if df.loc[bravo]['movie']==event and toein==0:
                                                toein=1
                                                certification=df.loc[bravo]['certification']
                                                language=df.loc[bravo]['language']
                                                formt=df.loc[bravo]['format']
                                                directedby.append(sg.T(df.loc[bravo]['directed by']))
                                                cast.append(sg.T(df.loc[bravo]['cast']))
                                                genre.append(sg.T(df.loc[bravo]['genre']))



                                
                        
                                  layout1=[[sg.T('-----------------------------On '+showdate+'--------------------',justification='center')],
                                           imagebutton,
                                        [sg.T(event.upper(),size=(8,1),font=("arial",15)),sg.T('-'+certification+ ' - '+language+formt)],
                                           genre,
                                           cast,
                                           directedby,
                                           

                                          timebutton,
                                          [sg.B('BACK')]]
                                  windo1=sg.Window('Showing',layout1)
                                  even,values=windo1.read()
                                  windo1.close()
                


                                  if even=='BACK' or even==sg.WIN_CLOSED:
                                              variable0=0
                                              variable1=0
                                              event=showdate
                                  else:
                                      for loki in range(len(df)):
                                          if df.loc[loki]['movie']==event and df.loc[loki]['date']==showdate and df.loc[loki]['showtime']==even :
                                                                    #variable0=10000000000000
                                                                    #variable1=10000000000000
                                              

                                                                    print(df.loc[loki]['movie'],df.loc[loki]['date'],df.loc[loki]['showtime'] )
                                                                    print(loki)
                                              
                                                                    u=0



                                                                    while u<1:

                                                                             noseatslist=[1,2,3,4,5,6,7,8,9,10]
                                                                             layout=[[sg.T("no of seats to book")],
                                                                                                        [sg.B("1"),sg.B("2"),sg.B("3"),sg.B("4"),sg.B("5"),sg.B("6"),sg.B("7"),sg.B("8"),sg.B("9"),sg.B("10")],
                                                                                                        [sg.B('back')]]
                                                                             window=sg.Window("noseats",layout,default_button_element_size=(3,1), auto_size_buttons=False)
                                                                             event,vals = window.read()
                                                                             window.close()
                                                                             i=0 
                                                                             if event==sg.WIN_CLOSED or event=='back' :
                                                                                 print('hi')
                                                                                 i=10000000000000
                                                                                 noseats=i-1
                                                                                 event=showdate
                                                                                                                          
     
     
     
                                                                             for ps in noseatslist:
                                                                                                                          if event==str(ps):
                                                                                                                                noseats=ps
                                                                                                                               
                                                                             p=0

                                                                             seatrow=[]
                                                                             seatno=[]
                                                                             index=[]
                                                                             silverseats=[]
                                                                             premiereseats=[]
                                                                             this=0
                                                                             while i<=noseats:
                                                                                    

                                                                                     print("file:",csvloc[loki])
                                                                                     a=pd.read_csv(csvloc[loki])
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
                                                                                                sumo.insert(5,sg.T("|   |"))
                                                                                                sumo.insert(0,sg.T("|   |"))
                                                                                                sumo.append(sg.T("|   |"))  
                                                                                     alphabets=["K","J","I","H","G","F","E","D","C","B","A"]     
                                                                                     if i==noseats and i==len(seatno) :

         
                                                                                                butt=sg.B("BOOK")
                                                                                            

                                                                                     else:
                                                                                                butt=sg.T("")
                                                                                     back=sg.B("back")
                                                                                     recancel=0

                                                                                     if i<=noseats:
                                                                                                lay=[[sg.T("SOAPANASUNDARI - 1",size=(55,1),justification='c',font=("arial",15))],
                                                                                                    [sg.T("EXT"),sg.T("                                                                                                                                "),sg.T("EXT")],
                                                                                                      kkk,
                                                                                                       jjj,
                                                                                                     [sg.T("|    ___  ___  ___  ___  ___  ___  ___  __  __  __|   |___   ___   ___  ___   ___   ___  ___   ___  ___ |")],
                                                                                                     iii,
                                                                                                     hhh,
                                                                                                     ggg,
                                                                                                     fff,
                                                                                                     eee,
                                                                                                     ddd,
                                                                                                     ccc,
                                                                                                     bbb,
                                                                                                     aaa,
                                                                                                     [sg.T("|    ___  ___  ___  ___  ___  ___  ___  __  __  __|   |___   ___   ___  ___   ___   ___  ___   ___  ___ |")],
                                                                                                                 [sg.T("____________________________________________________________________________________")],
                                                                                                    [sg.T("                     A  L  L         E  Y  E  S        T  H  I  S        W  A  Y         P  L  E  A  S  E               ")],
                                                                                                   [sg.T("____________________________________________________________________________________") ],
                                                                                                  [butt,back,sg.T("BKED  - already booked"),sg.T("               THIS   -  seat selected by you")],
                                                                                                  [sg.T("                           "),sg.T("SILVER(A-I): Rs 150",font=("arial",10)),sg.T("    "),sg.T("PREMIERE(J,K): Rs 170",font=("arial",10)),sg.T("   seats left for selection :"+str(noseats-i)+" ")]]
                                                                                                window=sg.Window("bookingscreen",lay,default_button_element_size=(4,1), auto_size_buttons=False)
                                                                                                event,vals = window.read()
 
                                                                                     if event=="back"  and len(seatno)==0 :
                                                                                             u=u-1
                                                                                             i=100000000000000
                                                                                             print("event==back  and len(seatno)==0 ")
                                                                                     if i!=noseats and i<noseats :
                                                                                             for dum in a.index:
                                                                                                     for col in range(1,11):
                                                                                                              if event== a.loc[dum][str(col)]:
                                                                                                                      for gg in range(len(a.loc[dum][str(col)])):                                                                                  
                                                                                                                                    print(event,a.loc[dum][str(col)])
                                                                                                                                    if gg==0:
                                                                                                                                              seatrow.append((a.loc[dum][str(col)])[0])
                                                                                                                                              print(seatrow)                                                                                                            
                                                                                                                                              
                                                                                                                      seatno.append(str(col))
                                                                                                                      print("seatno.append(str(col))",str(col))
                              
                                                                                                                      a.loc[dum][str(col)]=" THIS "
                                                                                                                      index.append(dum)
                                                                                                                      a.to_csv(csvloc[loki])
                                                                                                                      this=1
                                                                                                                      print("boked")
 
         
 
                                                                                     if this==1 and event=="back" and len(seatno)!=0:
                                                                                             i=i-1
                                                                                             a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                             print("this==1 and event==+back+ and len(seatno)!=0")
                                                                                             del(seatrow[-1])
                                                                                             del(seatno[-1])
                                                                                             del(index[-1])
                                                                        
                                                                                             print("index",index)
                                                                                             print("seatno",seatno)
                                                                                             print("seatrow",seatrow) 
                                                                                             a.to_csv(csvloc[loki])
                                                                                             window.close()
                                                                                     if this==1 and event==sg.WIN_CLOSED :
                                                                                             print(" this==1 and event==sg.WIN_CLOSED")
                                                                                             i=i-len(seatno)
                                                                                             this=0
                                                                                             for ip in range(len(seatno)):
                                                                                                     a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                                     del(seatrow[-1])
                                                                                                     del(seatno[-1])
                                                                                                     del(index[-1])
        
                                                                                                     a.to_csv(csvloc[loki])
                                                                                                     print("len(seatno)",len(seatno))
                                                                                                     print("index",index)
                                                                                                     print("seatno",seatno)
                                                                                                     print("seatrow",seatrow)
                                                                                                     window.close()
                                                                                     elif this==0 and event==sg.WIN_CLOSED :
                                                                                                     print("this==0 and event==sg.WIN_CLOSED")
                                                                                                     i=10000000000 
                                                                                                     u=u-1
                                                                                                     window.close()
                                                                                     if i!=len(seatno):
                                                                                                     window.close()
         
                                                                                     if i==len(seatno):
                                                                                                     window.close()
                                                                                                     if event=="BOOK":
                                                                                                         for hi in seatrow:
                                                                                                             if hi=="J" or hi=="K":
                                                                                                                 premiereseats.append((hi,seatno[seatrow.index(hi)]))
                                                                                                             else:
                                                                                                                 silverseats.append((hi,seatno[seatrow.index(hi)]))
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
                                                                                                                                               snacksbutton.append(sg.B(uniquesnackstype[tip]))
                                                                                                                                                                                                                                      

     
                                                                                                                                                                   
                                                                                                                                         
                                                                                                                                                  
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
                                                                                                                                                                          chatbutton.append(sg.B(refreshments.loc[jog]["item"]))
                                                                                                                                                                          refreshmentsname.append(refreshments.loc[jog]["item"])
                                                                                                                                                                          refreshmentsprice.append(refreshments.loc[jog]["cost"])
                                                                                                                                                                          
                                                                                                                                                                          refreshmentlisting.append([sg.T(refreshments.loc[jog]["item"],size=(15,1)),sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(15,1)),sg.B(refreshments.loc[jog]["item"])])
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
                                                                                                                                                     sandy=sandy-1
                                                                                                                                          sunny=sunny+1
                                                                                                                                          
                                                                                                                                                          











                                                                                                                                                                                                                                                        

 

                                                                                                               



                                                                                                         ticketcost=len(silverseats)*150 + len(premiereseats)*170
                                                                                                         onlinecharges=(len(silverseats) + len(premiereseats))*40
                                                                                                         totalcost=ticketcost+onlinecharges
                                                                                                         finalcost=totalcost+sum(orderedsnacksprice)
                                                                                                         
                                                                                                         bookingconfirm=[[sg.T("ARE u sure to pay for tickets")],
                                                                                                                         [sg.T("ticketcost    Rs:"+str(ticketcost))],
                                                                                                                         [sg.T("onlinecharges Rs:"+str(onlinecharges))],
                                                                                                                         [sg.T("totalcost     Rs:"+str(totalcost))],
                                                                                                                         [sg.T("snackscost     Rs:"+str(sum(orderedsnacksprice)))],
                                                                                                                          





                                                                                                                               [sg.T("Rs:"+str(finalcost))],
                                                                                                                     


                                                                                                                                 [sg.B("yes"),sg.B("no")]]
                                                                                                         work=sg.Window("confirmation",bookingconfirm,default_button_element_size=(3,1), auto_size_buttons=False)

                                                                                                         confirm,values=work.read()
                                                                                                         work.close()
                                                                                                         if confirm=="yes":
                                                                                                                     for gaythe in a.index:
                                                                                                                              for jaga in range(1,11):
                                                                                                                                     if a.loc[gaythe][str(jaga)]==" THIS ":
                                                                                                                                                  a.loc[gaythe][str(jaga)]="BKED"
                                                                                                                                                                                                                          








                                                                                                                     sg.popup("payment successful")
                                                                                                                     a.to_csv(csvloc[loki])

                                                                                                                     g=0
                                                                                                                     while g<1:
                                                                                                                            codeno=rd.randint(10000,99999)
                                                                                                                           #for xx in customer['codenos']:
                                                                                                                           #         if xx==codeno:
                                                                                                                             #                g=-1
                                                                                                                            g=g+1
                                                                                                                     codeno=str(codeno)
                                                                                                                     ww=0
                                                                                                                     while ww<1:
                                                                                                                             num=[[sg.Text("enter your phone number")],[sg.Input()],
                                                                                                                                  [sg.T("enter your name")],[sg.Input()],                                                                        

                                                                                                                                   [sg.Button("ok")]]

                                                                                                                             tata=sg.Window("number",num)
                                                                                                                             ting,vals=tata.read()
                                                                                                                             tata.close()
                                                                                                                             number=(vals[0])
                                                                                                                             customername=vals[1]

                                                                                                                             number=str(number)
                                                                                                                             if len(number)!=10 or ting==sg.WIN_CLOSED :
                                                                                                                                           sg.popup("enter valid number")
                                                                                                                                           ww=ww-1
                                                                                                                             ww=ww+1    

                                                                                                                      #for you in range(len(silvertickets)):
                                                                                                                                         #   customer.loc[max(customer)+1]=codeno,number
                                                                                                                      #for you in range(len(premieretickets)):
                                                                                                                                         #   customer.loc[max(customer)+1]=codeno,number
                                                                                                                                                                                                                     

                                                                                                          


                                                                                                                       #customersnacks.to_csv("customer snacks.csv")
                                                                                                                       #customer.to_csv("customer.csv")
                                                                                                                     sg.popup("your code number is:",codeno)

                                                                                                                     sg.popup("Thank you for booking.",
                                                                                                                           "view your details in MY history")
                                                                                                                     vari=vari-1
                                                                                                                     variable1=variable1+1
                                                                                                                      
                                                                                                         
                                                                                                         else:
                                                                                                                     print("back")
                                                                                                                     event=showdate
                                                                                                                     sandy=sandy-1
                                                                                                                    
                                                                                                                     recancel=1
                        
                                                                                                                     zing=index
                                                                                                                     for gaythe in range(len(zing)):
                                                                                                                                a.loc[zing[gaythe]][seatno[gaythe]]=seatrow[gaythe]+seatno[gaythe]
                                                                                                                                a.to_csv(csvloc[loki])
                                                                                                                               
                                                                                                            
                                                                                                                          

                                                                                                          
                                                                                                     

                                                                                                
                                                                                                                  
                                                                                                               
           
                                                                                                     else :
                                                                                                               i=i-1                                                                                              
                                                                                     i=i+1     
                                                                             u=u+1       

                                              












                                  sandy=sandy+1   
 
      variable0=variable0+1 
  if eventing=='EXIT' or event==sg.WIN_CLOSED:
      window0.close()
  vari=vari+1    
                                
            
            
                  
