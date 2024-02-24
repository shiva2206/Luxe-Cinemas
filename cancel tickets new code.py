import pandas as pd
import PySimpleGUI as sg
snacks = pd.read_csv("customer snacks.csv")
cus = pd.read_csv("customer.csv")
print(snacks)
print(cus)

num  =[[sg.Text("Enter Your Name:")],[sg.Input()],
             [sg.Text("Enter Your Phone Number:")],[sg.Input()],
             [sg.Text("Enter Your Code:")],[sg.Input()],
           [sg.Button("Cancel"),sg.Button("Submit")]]
    
tata = sg.Window("abc",num)
while True:
   
    ting,vals = tata.read()
    tata.close()
    if ting !="Submit":break
    name = vals[0].strip()
    phn = vals[1].strip()
    codn = vals[2].strip()
    if not phn.isdigit() or not codn.isdigit():
        sg.popup("Enter Valid Numbers")
        continue
    codn=int(codn)
    phn = int(phn)
    df = cus[(cus["name"]==name) & (cus["phnno"]==phn) & (cus["codenos"]==codn)]
    cusnaks = snacks[(snacks["name"]==name) & ( cus["phnno"]==phn )& (snacks["codenos"]==codn)]
    
    if len(df)!=0:            
        columns_to_display =['date', 'movie', 'showtime', 'seat', 'no', 'seattype', 'cost', 'programtime']
        # Define the PySimpleGUI layout
        df_selected = df[columns_to_display]
        
# Define the PySimpleGUI layout
        lout = [[sg.Text("Ticket Details")],
            [sg.Table(values=df_selected.values.tolist(),
                      headings=df_selected.columns.tolist(),
                      display_row_numbers=False,
                      auto_size_columns=False,
                      justification='right',
                      num_rows=min(25, len(df_selected)),
                      enable_events=True,
                      key='-TABLE-')],
                [[],[sg.Text("Snacks Details")],sg.Table(values = cusnaks.values.tolist(),
                                                         headings = cusnaks.columns.tolist(),
                                                         justification='right')] if len(cusnaks)!=0 else [],
            [[sg.Text("Total Ticket Cost: Rs " + str(sum(df["cost"]))), sg.Text("Total Snacks Cost: Rs " + str(sum(cusnaks["cost"]))) ] ],    
            [sg.Button('Exit'),sg.Button("Ok")]
        ]

        # Create the window
        wind = sg.Window('DataFrame Display', lout, resizable=True)

        # Event loop
        while True:
            eve, vlues = wind.read()

            if eve == sg.WINDOW_CLOSED or event == 'Exit':
                break
            if eve=="Ok":
                pass
            
        # Close the window
        window.close()
    
        
    else:
        sg.popup("Doesn't Exist")
        
    