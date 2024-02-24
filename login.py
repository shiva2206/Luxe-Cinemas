import PySimpleGUI as sg
import pandas as pd
import mysql.connector as mc
import datetime as dt
from datetime import datetime
import matplotlib.pyplot as plt

def unique_value(dataframe,column):
    lt=[]
    for var in dataframe[column]:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)


def dataframe(instruction):
      opodu=""
      mydb=mc.connect(
        host='localhost',
        database='test',
        user='root',
#         password='Mysql@123'
        password='#Mysql123'
        )
      cursor=mydb.cursor()
      cursor.execute(instruction)
      
      mydb.commit()
      return ""

def dataframefetchall(instruction):
      mydb=mc.connect(
        host='localhost',
        database='test',
        user='root',
        password='#Mysql123'
        )
      cursor=mydb.cursor()
      cursor.execute(instruction)
      record=cursor.fetchall()
      empdf=pd.DataFrame(record,columns=cursor.column_names)
      return empdf    






now=dt.datetime.now()
login=dataframefetchall("select * from pullingo")
login=login.set_index("id")

movieinfo=pd.read_csv("movie timing pro.csv")
movieinfo=movieinfo.set_index("_")
print(movieinfo)
df=movieinfo
future=movieinfo

dayaftertomorrow=dt.datetime.now()+dt.timedelta(2)
print(movieinfo)
for ggwp in df.index:
        timeobj=df.loc[ggwp]['date']+(" ")+df.loc[ggwp]['programtime']
        timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")
        timeformatobj=df.loc[ggwp]['date']
        timeformatfut=datetime.strptime(timeformatobj,"%d-%m-%Y")
        timeformatstr=timeformat.strftime("%d-%m-%Y %H:%M")
        timeformatday,timeformattime=timeformatstr.split(' ')
                         
        if timeformat<now  :
                df=df.drop([ggwp])
        if timeformatfut < dayaftertomorrow :
                future=future.drop([ggwp])
print(",",movieinfo)                
                                
originalscreen=["Mseat1.csv","Mseat2.csv","Mseat3.csv","Mseat4.csv","Mseat5.csv","Mseat6.csv","Tseat1.csv","Tseat2.csv","Tseat3.csv","Tseat4.csv","Tseat5.csv","Tseat6.csv","Wseat1.csv","Wseat2.csv","Wseat3.csv","Wseat4.csv","Wseat5.csv","Wseat6.csv","THseat1.csv","THseat2.csv","THseat3.csv","THseat4.csv","THseat5.csv","THseat6.csv",'Fseat1.csv', 'Fseat2.csv', 'Fseat3.csv','Fseat4.csv', 'Fseat5.csv', 'Fseat6.csv', 'Sseat1.csv', 'Sseat2.csv', 'Sseat3.csv', 'Sseat4.csv', 'Sseat5.csv', 'Sseat6.csv', 'SUseat1.csv', 'SUseat2.csv', 'SUseat3.csv', 'SUseat4.csv', 'SUseat5.csv', 'SUseat6.csv']

customer=pd.read_csv("customer.csv")


customersnacks=pd.read_csv("customer snacks.csv")


c=0
while  c<1: 
    layout=[[sg.Button("admin",size=(25,1))],
            [sg.Button("manager",size=(25,1))],
          
            [sg.Button("close",size=(25,1))]]
    window=sg.Window("LOGIN AS",layout)
    event,vals = window.read()
    window.close()
    d=0
    while d<1:
        if event=="admin" or event=="manager":
             layout=[[sg.Text("name")],[sg.Input()],
                     [sg.Text("password")],[sg.Input()],
                 [sg.Button("submit")],[sg.Button("back")]]
             window=sg.Window("details",layout)
             eve,vals = window.read()
             window.close()
             name=vals[0]
             password=vals[1]
             
             if eve=="back" or eve==sg.WIN_CLOSED :
                 c=c-1
        
             elif eve=="submit":
                 noo=1
                 for i in login.index:
                     e=0
                     
                     while e<1:
                        if str(login.loc[i]["name"])==str(name) and str(login.loc[i]["password"])==str(password) and login.loc[i]["dept"].lower()==event:
                               
                            noo=0
                            if event=="ADMIN(owner)":
                                layout=[[sg.Button("re-set MYdetails",size=(25,1))],
                                        [sg.Button("view bookingscreen",size=(25,1))],
                                        
                                        [sg.Button("movieshow INFO",size=(25,1))],
                                             [sg.B("SHOW HISTORY",size=(25,1))],
                                             [sg.B("GRAPHS",size=(25,1))],
                                    [sg.Button("back"),sg.Button("log out")]]
                                window=sg.Window(event,layout)
                                eventing,vals = window.read()
                                window.close()
                            else:
                                layout=[[sg.Button("re-set employee details",size=(25,1))],
                                         [sg.Button("re-set MYdetails",size=(25,1))],    
                                        [sg.Button("view bookingscreen",size=(25,1))],
                                        
                                        [sg.Button("movieshow INFO",size=(25,1))],
                                        [sg.B("SHOW HISTORY",size=(25,1))],     
                                        [sg.B("Update shows",size=(25,1))],
                                         [sg.B("GRAPHS",size=(25,1))],   
                                    [sg.Button("back"),sg.Button("log out")]]
                                window=sg.Window(event,layout)
                                eventing,vals = window.read()
                                window.close()
                            if eventing=="log out":
                                c=c-1
                            elif eventing=="back" or eventing==sg.WIN_CLOSED:
                                d=d-1
                            elif eventing=="re-set employee details":
                                employee=dataframefetchall("select * from employee")
                                employee=employee.set_index("id")
                                h=0
                                while h<1:
                                    layout=[[sg.T("whats your aim")],[sg.B("back"),sg.B("Update"),sg.B("Add")]]
                                    window=sg.Window("details",layout)
                                    pat,cummins=window.read()
                                    window.close()
                                    if pat=="Update" :

                                        rider=0
                                        indexid=list(employee.index)
                                        while rider <len(indexid) :
                                            robi=indexid[rider]

                                                          
                                                                 
                                            layout=[[sg.T("current details")],
                                                    [sg.T("name:      "),sg.InputText(employee.loc[robi]["name"])],
                                                                     
                                                    [sg.T("place:      "),sg.InputText(employee.loc[robi]["residence"])],
                                                    [sg.T("number;    "),sg.InputText(employee.loc[robi]["mobileno"])],
                                                    [sg.T("salary;    "),sg.InputText(employee.loc[robi]["salary"])],
                                                    [sg.T("dept;    "),sg.InputText(employee.loc[robi]["dept"])],
                                                    [sg.T("post;    "),sg.InputText(employee.loc[robi]["post"])],
                                                    [sg.B("update"),sg.B("Delete"),sg.B("Previous"),sg.B("Next"),sg.B("back")]]
                                                       
                                            window=sg.Window("details",layout)
                                            ian,vali=window.read()
                                            window.close()
                                                            
                                                            
                                            if ian=="update" :
                                                               
                                                jack=0
                                                if len(vali[0])>4:
                                                        jack=jack+1
                                                else:
                                                        sg.popup("name char  should be greater than 4")
                                                if len(vali[1])>3:
                                                        jack=jack+1
                                                else:
                                                        sg.popup("place char should be greater than 3")

                                                if len(vali[2])==10:
                                                    numberall=list(employee.mobileno)
                                                    numberall.remove(employee.loc[robi]["mobileno"])
                                                    booyah=0
                                                    for kolu in numberall:
                                                        if str(kolu)==str(vali[3]):
                                                            booyah=booyah+1
                                                    if booyah==0:
                                                        jack=jack+1
                                                    else:
                                                        sg.popup("entered number already exist")
                                                else:
                                                    sg.popup("number digit should be greater than 10")
                                                if len(vali[3])>=4:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("salaray is too low")
                                                if len(vali[4])>2:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("enter correct department")
                                                if len(vali[5])>3:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("enter correct post")
                                                if jack==6:
                                                    sg.popup("updated")    
                                                                   
                                                    employee=dataframe('update employee set name='+'"'+vali[0]+'"'+','+'dept='+'"'+vali[4]+'"'+','+'post='+'"'+vali[5]+'"'+','+'salary='+vali[3]+','+'mobileno='+'"'+vali[2]+'"'+','+'residence='+'"'+vali[1]+'"'+' where id='+str(robi))
                                                    employee=dataframefetchall("select * from employee")
                                                    employee=employee.set_index("id")
                                                    rider=0
                                                    indexid=list(employee.index)
                                                                   

                                            elif ian=="Delete":
                                                layout=[[sg.T("Are u sure you want to delete")],
                        
                                                        [sg.B("Yes"),sg.B("No")]]
                                                       
                                                window=sg.Window("details",layout)
                                                kaka,po=window.read()
                                                window.close()
                                                if kaka=="Yes":
                                                     dele=dataframe("delete from employee where id="+str(robi))
                                                     employee=dataframefetchall("select * from employee")
                                                     employee=employee.set_index("id")
                                                     indexid=list(employee.index)
                                            elif ian=="Next":
                                                    
                                                if rider==len(indexid)-1:
                                                        
                                                    rider=0
                                                                    
                                                else:
                                                                    
                                                    rider=rider+1
                                                                     
                                            elif ian=="Previous":
                                                                 
                                                if rider==0:
                                                    rider=len(indexid)-1
                                                                       
                                                                     
                                                else:    
                                                    rider=rider-1
                                                                       
                                            else:
                                                break
                                            
            
                                
                                    elif pat== "Add":
                                        employee=dataframefetchall("select * from employee")
                                        employee=employee.set_index("id")
                                        tring=0
                                              
                                        while tring<1:
                                            
                                            layout=[[sg.T("current details")],
                                                    [sg.T("name:      "),sg.Input()],
                                                                     
                                                    [sg.T("place:      "),sg.Input()],
                                                    [sg.T("number;    "),sg.Input()],
                                                    [sg.T("salary;    "),sg.Input()],
                                                    [sg.T("dept;    "),sg.Input()],
                                                    [sg.T("post;    "),sg.Input()],
                                                    [sg.B("update"),sg.B("back")]]
                                                       
                                            window=sg.Window("details",layout)
                                            ian,vali=window.read()
                                            window.close()
                                                                 
                                            if ian=="update" :
                                                               
                                                jack=0
                                                if len(vali[0])>4:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("name char  should be greater than 4")
                                                              

                                                if len(vali[1])>3:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("place char should be greater than 3")

                                                if len(vali[2])==10:
                                                                 
                                                    jack=jack+1
                                                                  
                                                else:
                                                    sg.popup("number digit should be greater than 10")
                                                if len(vali[3])>=4:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("salaray is too low")
                                                if len(vali[4])>2:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("enter correct department")
                                                if len(vali[5])>3:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("enter correct post")
                                                                   
                                                if jack==6:
                                                                   
                                                    employee=dataframe("insert into employee values"+str(tuple((max(employee.index)+1,vali[0],vali[4],vali[5],int(vali[3]),vali[2],vali[4]))))    
                                                    employee=dataframefetchall("select * from employee")
                                                    employee=employee.set_index("id")
                                                    sg.popup("Added")
                                            
                                                else:
                                                                   
                                                    tring=tring-1
                                            else:
                                                    h=h-1
                                            
                                            tring=tring+1
                        
                                          
                                            
                                            
                                            
                                    h=h+1
                                    e=e-1
                                        
                            elif eventing=="re-set MYdetails":
                                    g=0
                                    while g<1:  
                                       layout=[[sg.T("current details")],[sg.T("name:      "),sg.InputText(login.loc[i]["name"])],[sg.T("password:"),sg.InputText(login.loc[i]["password"])],[sg.T("place:      "),sg.InputText(login.loc[i]["residence"])],[sg.T("number;    "),sg.InputText(login.loc[i]["mobileno"])],
                                            [sg.B("update"),sg.B("back")]]
                                    
                                       window=sg.Window("details",layout)
                                       sacrifice,vali= window.read()
                                       window.close()
                                       if sacrifice=="update":
                                           jack=0
                                           if len(vali[0])>4:
                                                jack=jack+1
                                           else:
                                                sg.popup("name char  should be greater than 4")
                                           if len(vali[1])>5:
                                                passwordall=list(login.password)
                                                passwordall.remove(login.loc[i]["password"])
                                                booyah=0
                                                for kolu in passwordall:
                                                   if kolu==vali[1]:
                                                      booyah=booyah+1
                                                if booyah==0:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("please change your password")
                                            
                                           else:    
                                                sg.popup("password char should be greater than 4")

                                           if len(vali[2])>3:
                                                jack=jack+1
                                           else:
                                                sg.popup("place char should be greater than 3")

                                           if len(vali[3])==10:
                                                numberall=list(login.mobileno)
                                                numberall.remove(login.loc[i]["mobileno"])
                                                booyah=0
                                                for kolu in numberall:
                                                    if str(kolu)==str(vali[3]):
                                                        booyah=booyah+1
                                                if booyah==0:
                                                    jack=jack+1
                                                else:
                                                    sg.popup("entered number already exist")
                                                                       
                                           else:
                                                sg.popup("number digit should be greater than 10")
                                           if jack==4:
                                                login=dataframe('update pullingo set name='+'"'+vali[0]+'"'+','+'mobileno='+'"'+vali[3]+'"'+','+'residence='+'"'+vali[2]+'"'+','+'password='+'"'+vali[1]+'"'+' where id='+str(i))
                                                login=dataframefetchall("select * from pullingo")
                                                login=login.set_index("id")
                                                e=e-1
                                                
                                                sg.popup("updated")
                                                name=vali[0]
                                                password=vali[1]
                                                
                                              
                                           else:
                                                g=g-1
                                       else:
                                              g=g
                                              e=e-1
                                              
                                              
                                       g=g+1
                                     
                     
                            elif eventing=="GRAPHS":
                                yendi=0
                                while yendi <1:
                                    layout=[[sg.Button("MOVIES  vs   SEATS",size=(25,1))],
                                               [sg.Button("refreshments graph",size=(25,1))],
                                          [sg.Button("seats vs days",size=(25,1))],
                                            [sg.Button("seats vs time",size=(25,1))],
                                           
                                          [sg.Button("back")]]
                                    window=sg.Window(event,layout)
                                    eting,vals = window.read()
                                    window.close()
                                    if eting=="MOVIES  vs   SEATS":
                                        oldmovieinfo=movieinfo
                                        for kgh in df.index:
                                                   oldmovieinfo.drop([kgh])
                                                      
                                        movienames=unique_value(movieinfo,"movie")
                                        seatsfilledlist=[]
                                        for asd in movienames:
                                                   oldies=oldmovieinfo[oldmovieinfo.movie==asd]
                                                   seatsfilledlist.append(sum(oldies.seatsfilled)//len(oldies))
                                                   
                                        plt.bar(movienames,seatsfilledlist)
                                        plt.xlabel("movie names")
                                        plt.ylabel("number of seats filled (total seats=110)")
                                        plt.title("average seats filled")
                                        plt.grid()
                                        plt.show(block=False)
                                        
                                      
                                       
                                    elif eting=="refreshments graph":
                                         customersnacksdates=unique_value(customersnacks,"date")
                                         datessbutton=[]
                                         
                                         for iop in customersnacksdates:
                                             datessbutton.append([sg.B(iop)])
                                         datessbutton.append([sg.B("back")])    
                                         layout=datessbutton
                                         window=sg.Window("dates",layout)
                                         spea,ker = window.read()
                                         window.close()
                                         if spea in customersnacksdates:
                                                             
                                         
                                                partcustomersnacks=customersnacks[customersnacks.date==spea]
                                                types=unique_value(partcustomersnacks,"type")
                                                typelist=[]
                                                for asd in types:
                                                           oldies=partcustomersnacks[partcustomersnacks.type==asd]
                                                           typelist.append(len(oldies))
                                          
                                                plt.bar(types,typelist)
                                                plt.xlabel("snacks type ")
                                                plt.ylabel("quantity of snacks")
                                                plt.title("refreshment quantity vs snacks type on "+spea)
                                                plt.grid()
                                                plt.show(block=False)
                                                
                                    elif eting=="seats vs days":
                                        uniquedates=unique_value(movieinfo,"date")
                                        silve=[]
                                        premer=[]
                                        for qst in uniquedates:
                                            
                                           rummy=movieinfo[movieinfo.date==qst]
                                           silve.append(sum(rummy.silver)/len(rummy))
                                           premer.append(sum(rummy.premiere)/len(rummy))
                                           print(rummy)
                                        plt.bar(uniquedates,silve)
                                        plt.bar(uniquedates,premer)
                                        plt.xlabel("dates")
                                        plt.ylabel("no of seats(tot silver=90,tot premiere =20)")
                                        plt.title("average no of seats booked")
                                        plt.legend()
                                        plt.grid()
                                        plt.show(block=False)
                                    elif eting=="seats vs time":    
                                        uniquetime=unique_value(movieinfo,"showtime")
                                        tota=[]
                                        for qst in uniquetime:
                                            
                                           rummy=movieinfo[movieinfo.showtime==qst]
                                           tota.append(sum(rummy.seatsfilled)/len(rummy))
                                           
                                        plt.plot(uniquetime,tota)
                                        
                                        plt.xlabel("time")
                                        plt.ylabel("no of seats(tot number of tickets =110)")
                                        plt.title("average no of seats booked")
                                        plt.legend()
                                        plt.grid()
                                        plt.show(block=False)   
                                           
                                        
                                            

                                    yendi=yendi+1
                                e=e-1
                                     
                                    
                                        
                            elif eventing=="movieshow INFO":
                                jakpot=0
                                dfindex=list(df.index)
                                while jakpot<len(df):
                                    robi=dfindex[jakpot]
                                    if robi in future.index:
                                        djb=sg.B("delete")
                                    else:
                                        djb=sg.T("")
                                    
                                    layout=[[sg.T("      Movie details   " )],
                                            [sg.T("date         :"),sg.T(df.loc[robi]["date"])],
                                                
                                            [sg.T("movie         :"),sg.InputText(df.loc[robi]["movie"])],
                                            [sg.T("language      :"),sg.T(df.loc[robi]["language"])],
                                            [sg.T("showtime      :"),sg.T(df.loc[robi]["showtime"])],
                                            [sg.T("certification :"),sg.InputText(df.loc[robi]["certification"])],
                                            [sg.T("image file 1  :"),sg.InputText(df.loc[robi]["image file 1"])],
                                            [sg.T("image file 2  :"),sg.InputText(df.loc[robi]["image file 2"])],
                                            [sg.T("format        :"),sg.InputText(df.loc[robi]["format"])],
                                            [sg.T("directed by   :"),sg.InputText(df.loc[robi]["directed by"])],
                                            [sg.T("cast          :"),sg.InputText(df.loc[robi]["cast"])],
                                            [sg.T("genre         :"),sg.InputText(df.loc[robi]["genre"])],
                                            [sg.T("bookingscreen :"),sg.T(df.loc[robi]["bookingscreen"])],
                                            [sg.T("trailer       :"),sg.InputText(df.loc[robi]["trailer"])],
                                            [sg.T("seatsfilled   :"),sg.T(df.loc[robi]["seatsfilled"])],
                                            [sg.T("silver type   :"),sg.T(df.loc[robi]["silver"])],
                                            [sg.T("premiere type :"),sg.T(df.loc[robi]["premiere"])],

                                                   
                                            [sg.B("Previous"),sg.B("Next"),sg.B("update"),sg.B("graph"),djb,sg.B("back")]]
                                                       
                                    window=sg.Window("details",layout)
                                    iron,man=window.read()
                                    window.close()
                                    if iron=="Next":
                                        if jakpot==len(df)-1:
                                            jakpot=0
                                        else:
                                            jakpot=jakpot+1
                                    elif iron=="Previous":
                                        if jakpot==0:
                                            jakpot=len(df)-1
                                        else:
                                            jakpot=jakpot-1
                                    elif iron=="update":
                                        fz=list(df[df.movie==df.loc[robi]["movie"]].index)
                                        for dfg in fz:
                                            movieinfo.loc[dfg,"movie"]=man[0]
                                            movieinfo.loc[dfg,"certification"]=man[1]
                                            movieinfo.loc[dfg,"image file 1"]=man[2]
                                            movieinfo.loc[dfg,"image file 2"]=man[3]
                                            movieinfo.loc[dfg,"format"]=man[4]
                                            movieinfo.loc[dfg,"directed by"]=man[5]
                                            movieinfo.loc[dfg,"cast"]=man[6]
                                            movieinfo.loc[dfg,"genre"]=man[7]
                                            movieinfo.loc[dfg,"trailer"]=man[8]
                                            movieinfo.to_csv("movie timing pro.csv")

                                            df=movieinfo



                                            for ggwp in df.index:
                                                    timeobj=df.loc[ggwp]['date']+(" ")+df.loc[ggwp]['programtime']
                                                    timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")
                                                    timeformatobj=df.loc[ggwp]['date']
                                                    timeformatfut=datetime.strptime(timeformatobj,"%d-%m-%Y")
                                                    timeformatstr=timeformat.strftime("%d-%m-%Y %H:%M")
                                                    timeformatday,timeformattime=timeformatstr.split(' ')
                         
                                                    if timeformat<now  :
                                                            df=df.drop([ggwp])
                                            
                                            
                                    elif iron=="delete":
                                        df=df.drop([robi])
                                        future=future.drop([robi])
                                        movieinfo=movieinfo.drop([robi])
                                        movieinfo.to_csv("movie timing pro.csv")
                                        jakpot=0
                                        dfindex=list(df.index)
                                        sg.popup("deleted")
                                    elif iron=="graph":
                                        xxxx=[df.loc[robi]["silver"]//90,df.loc[robi]["premiere"]//20]
                                        print(xxxx)
                                        plt.bar(["silver","premiere"],xxxx)
                                        plt.yticks([0,1],xxxx[0])
                                        plt.show()
                                        
                                        
                                    else :
                                        e=e-1
                                        break
                                                    
                            elif eventing=="SHOW HISTORY":
                                    jakpot=0
                                    movieinfoindex=list(movieinfo.index)
                                    while jakpot<len(movieinfo):
                                           robi=movieinfoindex[jakpot]
                                           layout=[[sg.T("      Movie details   " )],
                                                   [sg.T("date         :"),sg.T(movieinfo.loc[robi]["date"])],
                                                
                                                   [sg.T("movie         :"),sg.T(movieinfo.loc[robi]["movie"])],
                                                   [sg.T("language      :"),sg.T(movieinfo.loc[robi]["language"])],
                                                   [sg.T("showtime      :"),sg.T(movieinfo.loc[robi]["showtime"])],
                                                   [sg.T("certification :"),sg.T(movieinfo.loc[robi]["certification"])],
                                                   [sg.T("image file 1  :"),sg.T(movieinfo.loc[robi]["image file 1"])],
                                                   [sg.T("image file 2  :"),sg.T(movieinfo.loc[robi]["image file 2"])],
                                                   [sg.T("format        :"),sg.T(movieinfo.loc[robi]["format"])],
                                                   [sg.T("directed by   :"),sg.T(movieinfo.loc[robi]["directed by"])],
                                                   [sg.T("cast          :"),sg.T(movieinfo.loc[robi]["cast"])],
                                                   [sg.T("genre         :"),sg.T(movieinfo.loc[robi]["genre"])],
                                                   [sg.T("bookingscreen :"),sg.T(movieinfo.loc[robi]["bookingscreen"])],
                                                   [sg.T("trailer       :"),sg.T(movieinfo.loc[robi]["trailer"])],


                                                   
                                                   [sg.B("Previous"),sg.B("Next"),sg.B("back")]]
                                                       
                                           window=sg.Window("details",layout)
                                           iron,man=window.read()
                                           window.close()
                                           if iron=="Next":
                                               if jakpot==len(movieinfo)-1:
                                                    jakpot=0
                                               else:
                                                    jakpot=jakpot+1
                                           elif iron=="Previous":
                                               if jakpot==0:
                                                    jakpot=len(movieinfo)-1
                                               else:
                                                   jakpot=jakpot-1
                                           else:
                                                e=e-1
                                                break
                                                    
                                    
                            elif eventing=="Update shows":
                                    
                                layout=[[sg.T("whats your aim")],[sg.B("back"),sg.B("Add New movie"),sg.B("Upload existing movie"),]]
                                window=sg.Window("details",layout)
                                pat,cummins=window.read()
                                window.close()
                                        
                                now=dt.datetime.now()
                                nowstr=now.strftime("%d-%m-%Y %H:%M:%S")
                                today,time=nowstr.split(' ')
                                todayday,todaymonth,todayyear=today.split('-')
                                tomorrow=dt.datetime.now()+dt.timedelta(1)
                                dayaftertomorrow=dt.datetime.now()+dt.timedelta(2)
                                dayaftertomorrow1=dt.datetime.now()+dt.timedelta(2)
                                
                                        
                                day4=dt.datetime.now()+dt.timedelta(3)
                                day5=dt.datetime.now()+dt.timedelta(4)
                                day6=dt.datetime.now()+dt.timedelta(5)
                                day7=dt.datetime.now()+dt.timedelta(6)
                                         
                                        
                                tomorrow=tomorrow.strftime("%d-%m-%y")
                                tomorrowday,tomorrowmonth,tomorrowyear=tomorrow.split('-')
                                        
                                        
                                dayaftertomorrow=dayaftertomorrow.strftime("%d-%m-%y")
                                dayaftertomorrowday,dayaftertomorrowmonth,dayaftertomorrowyear=dayaftertomorrow.split('-')
                                        

                                day4=day4.strftime("%d-%m-%y")
                                day4day,day4month,day4year=day4.split('-')
                                        

                                day5=day5.strftime("%d-%m-%y")
                                day5day,day5month,day5year=day5.split('-')
                                        

                                day6=day6.strftime("%d-%m-%y")
                                day6day,day6month,day6year=day6.split('-')
                                        

                                day7=day7.strftime("%d-%m-%y")
                                day7day,day7month,day7year=day7.split('-')

                                        
                                 
                                        
                                if todayday[0]=="0":
                                    todayday=todayday.replace("0","",1)
                                if todaymonth[0]=="0":
                                    todaymonth=todaymonth.replace("0","",1)
                                if tomorrowday[0]=="0":
                                    tomorrowday=tomorrowday.replace("0","",1)        
                                if tomorrowmonth[0]=="0":
                                    tomorrowmonth=tomorrowmonth.replace("0","",1)
                                if dayaftertomorrowday[0]=="0":
                                    dayaftertomorrowday=dayaftertomorrowday.replace("0","",1)
                                if dayaftertomorrowmonth[0]=="0":
                                    dayaftertomorrowmonth=dayaftertomorrowmonth.replace("0","",1)
                                if day4day[0]=="0":
                                    day4day=day4day.replace("0","",1)
                                if day4month[0]=="0":
                                    day4month=day4month.replace("0","",1)
                                if day5day[0]=="0":
                                    day5day=day5day.replace("0","",1)
                                if day5month[0]=="0":
                                    day5month=day5month.replace("0","",1)
                                if day6day[0]=="0":
                                    day6day=day6day.replace("0","",1)
                                if day6month[0]=="0":
                                    day6month=day6month.replace("0","",1)
                                if day7day[0]=="0":
                                    day7day=day7day.replace("0","",1)
                                if day7month[0]=="0":
                                    day7month=day7month.replace("0","",1)
                                             

                                today=todayday+'/'+todaymonth+'/'+todayyear
                                tomorrow=tomorrowday+'/'+tomorrowmonth+'/'+todayyear[:2]+tomorrowyear
                                dayaftertomorrow=dayaftertomorrowday+'/'+dayaftertomorrowmonth+'/'+todayyear[:2]+dayaftertomorrowyear
                                day4=day4day+'/'+day4month+'/'+todayyear[:2]+day4year
                                day5=day5day+'/'+day5month+'/'+todayyear[:2]+day5year
                                day6=day6day+'/'+day6month+'/'+todayyear[:2]+day6year
                                day7=day7day+'/'+day7month+'/'+todayyear[:2]+day7year
                                        
                                        
                                datestot=[today,tomorrow,dayaftertomorrow,day4,day5,day6,day7]
                                        
                                if  pat=="Add New movie":
                                                 
                                    programtimes=unique_value(movieinfo,"programtime")
                                    certification=unique_value(movieinfo,"certification")
                                    shows=list(movieinfo.showtime)
                                                 
                                    screen=list(movieinfo.bookingscreen)
                                    layout=[[sg.T("date:            ",size=(12,1)),sg.Listbox(datestot,key="0")],
                                            [sg.T("program time:    ",size=(12,1)),sg.Listbox(programtimes,key="1")],
                                            [sg.T("movie name:      ",size=(12,1)),sg.Input()],
                                            [sg.T("language:        ",size=(12,1)),sg.Listbox(["tamil","english","telugu","hindi","malayalam"],key="3")],
                                                           
                                            [sg.T("certification:  ",size=(12,1)),sg.Listbox(certification,key="4")],
                                            [sg.T("imagefile 1:     ",size=(12,1)),sg.Input()],
                                            [sg.T("imagefile 2:     ",size=(12,1)),sg.Input()],
                                            [sg.T("format:          ",size=(12,1)),sg.Listbox(["2D","3D"],key="7")],
                                            [sg.T("directed by:     ",size=(12,1)),sg.Input()],
                                            [sg.T("cast:           ",size=(12,1)),sg.Input()],
                                            [sg.T("genre:          ",size=(12,1)),sg.Input()],
                                            [sg.T("bookingscreen:  ",size=(12,1)),sg.Listbox(screen,key="11")],
                                            [sg.T("trailer         ",size=(12,1)),sg.Input()],
                                            [sg.B("update"),sg.B("back")]]
                                    window=sg.Window("details",layout)
                                    keer,thana=window.read()
                                    window.close()
                                    if keer=="update":
                                        if  thana["0"] and thana["1"] and thana["4"] and thana["3"] and thana["4"] and thana["7"] and thana["11"]:
                                            jaddu=0
                                            for ggwp in movieinfo.index:
                                                timeobj=movieinfo.loc[ggwp]['date']+(" ")+movieinfo.loc[ggwp]['programtime']
                                                timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")
                                                timeformatstr=timeformat.strftime("%d-%m-%Y %H:%M")
                                                timeformatday,timeformattime=timeformatstr.split(' ')
                         
                                                if timeformatday==thana["0"][0] and timeformattime==thana["1"][0]:
                                                                        
                                                    jaddu=1
                                            for kol in range(len(programtimes)):
                                                 if programtimes[kol]==thana["1"][0]:
                                                        showssel=shows[kol]

                                                        
                                                              
                                            if jaddu==0:
                                                movieinfo.loc[max(movieinfo.index)+1]=thana["0"][0],thana["1"][0],thana[0],thana["3"][0],showssel,thana["4"][0],thana[1],thana[2],thana["7"][0],thana[3],thana[4],thana[5],thana["11"][0],thana[6],0,0,0
                                                df.loc[max(movieinfo.index)+1]=thana["0"][0],thana["1"][0],thana[0],thana["3"][0],showssel,thana["4"][0],thana[1],thana[2],thana["7"][0],thana[3],thana[4],thana[5],thana["11"][0],thana[6],0,0,0
                                                
                                                movieinfo.to_csv("movie timing pro.csv")
                                                if dayaftertomorrow1 < datetime.strptime(thana["0"][0],"%d-%m-%Y"):
                                                        if len(future)==0:
                                                            future.loc[0]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0
                                                        else:
                                                            future.loc[max(future.index)+1]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0



                                            else:
                                                sg.popup("sorry chosse other date /time")
                                        else:
                                            sg.popup("select proplerly")
                                if pat=="Upload existing movie":
                                    hulk=0
                                    while hulk<1:
                                        movienames=unique_value(movieinfo,"movie")
                                        programtimes=unique_value(movieinfo,"programtime")
                                        shows=unique_value(movieinfo,"showtime")
                                        fakescreen=list(movieinfo.bookingscreen)
                                                 
                                        screen=[]
                                                 
                                        for hhh in originalscreen:
                                            kiclu=0
                                            for jjjj in fakescreen:
                                                if hhh==jjjj:
                                                    kiclu=1
                                            if kiclu==0:
                                                screen.append(hhh)
                                                seatis=pd.read_csv(hhh)
                                                seatis=seatis.set_index("_")
                                                for uyt in seatis.index:
                                                    for pqr in range(1,11):
                                                        seatis.loc[uyt,str(pqr)]=seatis.loc[uyt]["alphabets"]+str(pqr)
                                                seatis.to_csv(hhh)
                                                 #if len(screen)==0:
                                                  #       sg.popup("sorry not available")
                                                   #      e=e-1
                                                    #     break
                                              
                                        layout=[[sg.T("date:            ",size=(12,1)),sg.Listbox(datestot,key="0")],
                                                [sg.T("program time:    ",size=(12,1)),sg.Listbox(programtimes,key="1")],
                                                [sg.T("movie name:      ",size=(12,1)),sg.Listbox(movienames,key="2")],
                                                [sg.T("language:        ",size=(12,1)),sg.Listbox(["tamil","english","telugu","hindi","malayalam"],key="3")],
                                                           
                                                [sg.T("bookingscreen:  ",size=(12,1)),sg.Listbox(screen,key="5")],
                                                [sg.B("update"),sg.B("back")]]
                                        window=sg.Window("details",layout)
                                        keer,thana=window.read()
                                        window.close()
                                        if keer=="update":
                                            if  thana["0"] and thana["1"] and thana["2"] and thana["3"] and thana["5"]:
                                                jaddu=0
                                                for ggwp in movieinfo.index:
                                                    timeobj=movieinfo.loc[ggwp]['date']+(" ")+movieinfo.loc[ggwp]['programtime']
                                                    timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")
                                                    timeformatstr=timeformat.strftime("%d-%m-%Y %H:%M")
                                                    timeformatday,timeformattime=timeformatstr.split(' ')
                         
                                                    if movieinfo.loc[ggwp]['date']==thana["0"][0] and movieinfo.loc[ggwp]['programtime']==thana["1"][0]:
                                                                        
                                                        jaddu=1
                                                                               
                                                if jaddu==0:
                                                    for kol in range(len(programtimes)):
                                                        if programtimes[kol]==thana["1"][0]:
                                                            showssel=shows[kol]
                                                    for kjh in movieinfo.index:
                                                        if movieinfo.loc[kjh]["movie"]==thana["2"][0]:
                                                            certification=movieinfo.loc[kjh]["certification"]                               
                                                            imagefile1= movieinfo.loc[kjh]["image file 1"]                          
                                                            imagefile2= movieinfo.loc[kjh]["image file 2"]                         
                                                            format =    movieinfo.loc[kjh]["format"]                                  
                                                            directedby= movieinfo.loc[kjh]["directed by"]                      
                                                            cast      = movieinfo.loc[kjh]["cast"]         
                                                            genre     = movieinfo.loc[kjh]["genre"]
                                                            trailer   = movieinfo.loc[kjh]["trailer"]
                                                                    
                                                    movieinfo.loc[max(movieinfo.index)+1]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0
                                                    if len(df)==0:
                                                        df.loc[0]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0
                                                    else:
                                                        df.loc[max(df.index)+1]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0

                                                                          
                                                                         
                                                    movieinfo.to_csv("movie timing pro.csv")
                                                    if dayaftertomorrow1 < datetime.strptime(thana["0"][0],"%d-%m-%Y"):
                                                        if len(future)==0:
                                                            future.loc[0]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0
                                                        else:
                                                            future.loc[max(future.index)+1]=thana["0"][0],thana["1"][0],thana["2"][0],thana["3"][0],showssel,certification,imagefile1,imagefile2,format,directedby,cast,genre,thana["5"][0],trailer,0,0,0


                                                    
                                                    sg.popup("updated")
          

                                                else:
                                                    sg.popup("sorry chosse other date /time")
                                                    hulk=hulk-1
                                            else:
                                                sg.popup("select proplerly")
                                                hulk=hulk-1
                                                             
                                                 
                                        hulk=hulk+1
                                                 
                                                 
                                     
                                        
                                e=e-1

                            elif eventing=="view bookingscreen":
                                    f=0
                                    while f<1: 
                                         
                                         movies=list(df.movie)
                                         shows=list(df.showtime)
                                         dates=list(df.date)
                                         screen=list(df.bookingscreen)
                                         listscreen=[]
                                         for gan in range(len(shows)):
                                    
                                                listscreen.append([sg.B(movies[gan].upper()+"   "+ dates[gan]+"  -  "+shows[gan],size=(35,1),key=screen[gan])])
                                         listscreen.append([sg.B("back")])
                                    
                                         layout=listscreen
                                         window=sg.Window("details",layout)
                                         tik,vals = window.read()
                                         window.close()
                                         if tik=="back":
                                              e=e
                                         
                                         for dum in range(len(screen)):
                                             if tik==screen[dum]:
                                                 junga=pd.read_csv(screen[dum])
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
                                                 for var in junga.index:
                                                    for dor in range(1,11):
                                                            
                                                        rows[var].append(sg.T(junga.loc[var][str(dor)],size=(5,1)))
                                                 for sumo in rows: 
                                                    sumo.insert(-2,sg.T("|   |"))
                                                    sumo.insert(2,sg.T("|   |"))
                                                                                           
                                                    sumo.insert(0,sg.T("|   |"))
                                                    sumo.append(sg.T("|   |"))
                                                 lay=[[sg.T("LUXE CINEMAS",size=(55,1),justification='c',font=("arial",15))],
                                                      [sg.T("ShowDate:"+dates[dum],size=(25,1)),sg.T("Movie:"+movies[dum],size=(25,1)),sg.T("ShowTime:"+shows[dum],size=(25,1))],                                     
                                                      [sg.T("EXT"),sg.T("                                                                                                                                      "),sg.T("EXT")],
                                                        kkk,
                                                        jjj,
                                                        [sg.T("|   |   __  ___  ___  ___ _ |   |___  ___  ___  __  __  __   ___  ____  ___  ___  __  ___  |   |___   ___   ___ __   |   |")],
                                                        iii,
                                                        hhh,
                                                        ggg,
                                                        fff,
                                                        eee,
                                                        ddd,
                                                        ccc,
                                                        bbb,
                                                        aaa,
                                                        [sg.T("|   ___  ___ ___  ___  ___  |   |___  ___  ___  __  __  __   ___   ___   ___  _____   ___  |   |   ___  ___  ___  ___ __|")],                                 
                                                        [sg.T("____________________________________________________________________________________")],
                                                        [sg.T("                     A  L  L         E  Y  E  S        T  H  I  S        W  A  Y         P  L  E  A  S  E               ")],
                                                        [sg.T("____________________________________________________________________________________") ],
                                                        [sg.T("BKED  -  booked")],
                                                        [sg.B("back"),sg.T("SILVER(A-I): Rs 150",font=("arial",10)),sg.T("    "),sg.T("PREMIERE(J,K): Rs 170",font=("arial",10))]]
                                                 window=sg.Window("bookingscreen",lay,default_button_element_size=(4,1), auto_size_buttons=False)
                                                 bucket,vals = window.read()
                                                 window.close()
                                                 if bucket=="back" or bucket==sg.WIN_CLOSED:
                                                     f=f-1
                                         f=f+1                                                                 
                                    e=e-1
                        e=e+1            
                 if noo == 1:
                    d=d-1
                    sg.popup("your password or name is wrong")
        d=d+1  
    c=c+1 
