import pandas as pd



# #TO delete all details in customer snacks
# df = pd.read_csv("customer snacks.csv")
# df= df.iloc[0:0]
# df.to_csv('customer snacks.csv', index=False)
# 
# #To delete all datas in customer.csv
# cus = pd.read_csv("customer.csv")
# cus=cus.iloc[0:0]
# cus.to_csv("customer.csv",index =False)
# 
# 
# # #To make all seat filled to zero
# movtim = pd.read_csv("movie timing pro.csv")
# col_zero = ["seatsfilled","silver","premiere"]
# movtim[col_zero] =0
# movtim.to_csv("movie timing pro.csv",index = False)


# 
# # To remove all booked seats in all seats
# originalscreen=["Mseat1.csv","Mseat2.csv","Mseat3.csv","Mseat4.csv","Mseat5.csv","Mseat6.csv","Tseat1.csv","Tseat2.csv","Tseat3.csv","Tseat4.csv","Tseat5.csv","Tseat6.csv","Wseat1.csv","Wseat2.csv","Wseat3.csv","Wseat4.csv","Wseat5.csv","Wseat6.csv","THseat1.csv","THseat2.csv","THseat3.csv","THseat4.csv","THseat5.csv","THseat6.csv",'Fseat1.csv', 'Fseat2.csv', 'Fseat3.csv','Fseat4.csv', 'Fseat5.csv', 'Fseat6.csv', 'Sseat1.csv', 'Sseat2.csv', 'Sseat3.csv', 'Sseat4.csv', 'Sseat5.csv', 'Sseat6.csv', 'SUseat1.csv', 'SUseat2.csv', 'SUseat3.csv', 'SUseat4.csv', 'SUseat5.csv', 'SUseat6.csv']
# 
# 
# for k in originalscreen:
#     screen = pd.read_csv(k)
#     print(screen)
#     for i in range(len(screen)):
#         for j in range(1,11):
#             screen.at[i,str(j)] = screen.at[i,'alphabets']+str(j)
#     screen.to_csv(k,index=False)
#     print(screen)        
