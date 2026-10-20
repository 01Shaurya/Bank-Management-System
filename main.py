import os
import pandas as pd
import getpass 
import pickle
import datetime
import pytz



tz = pytz.timezone("Asia/Kolkata")
current_datetime = datetime.datetime.now(tz)
time=current_datetime.strftime('%I:%M %p , %d-%m-%Y ')

width=os.get_terminal_size().columns

def get_password():
   print("\033[32mPlease Enter Your Password:\t".center(width))
   password=getpass.getpass("-->")
   capital=any(x.isupper() for x in password)
   lower=any(x.islower() for x in password)
   number = 0
   symbol = 0
   symbols=list("!@#$%^&*_+-`~><|")
   for x in password:
      if x in symbols:
         symbol+=1
      elif x in "1234567890":
         number+=1
   security_requirements=capital and lower and (symbol>0) and (number>0)
   while security_requirements==False:
        print("\033[31mYour Password Do Not Fullfill The Security Requirements.".center(width))
        print("\033[32mPlease Enter Your Password".center(width))
        password=getpass.getpass("-->")

   else:
        print("\033[32mPlease Confirm Your Password:\t".center(width))
        confirm_password=getpass.getpass("-->")
        while password!=confirm_password:
          print("\033[31mThe Password You Entered For Confirming Do No Match The Actual Entered Password.".center(width))
          print("\033[32mPlease Confirm Your Password:\t".center(width))
          confirm_password=getpass.getpass("-->")
   return password     


class MANAGER:
   def __init__(self,admin_name,admin_password,):
      self.admin_name=admin_name
      self.admin_password=admin_password
   def add_account(self):
      
      print(("\033[32mEnter Account Number:".center(width)))
      account_number=int(input("-->"))
      
      
      if os.path.exists("Customer_Data.pkl"):
         customer_data=pd.read_pickle("Customer_Data.pkl")
         if account_number not in customer_data['Account Number']:
            print("\033[32mEnter Name Of The Person:".center(width))
            name=input("-->")
            print("\033[32mEnter Mobile".center(width))
            mobile_number=input("-->")
            print("\033[32mEnter Email".center(width))
            email=input("-->")
            print("\033[32mEnter Address".center(width))
            address=input("-->")
            print("\033[32mEnter Balance".center(width))
            balance=float(input("-->"))
            time_updated=time   
            data={"Account Number":[account_number],
                     "Name":[name],
                     "Mobile Number":[mobile_number],
                     "Email":[email],
                     "Address":[address],
                     "Balance":[balance] ,
                     "Time Updated":[time_updated]
                     }
               
            dataframe=pd.DataFrame(data)
            
            customer_data=pd.read_pickle("Customer_Data.pkl")
            merged_data=pd.concat([dataframe,customer_data], axis=0, ignore_index=True)
            merged_data.to_pickle("Customer_Data.pkl")
            print("\033[36mAccount Created Successfully.\n".center(width))    
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
            os.system("cls")


         else:  
            print("\033[31mThe Account Number You Entered, Already Exists.\n".center(width))    
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()

               
      else:
         print("\033[32mEnter Name Of The Person:".center(width))
         name=input("-->")
         print("\033[32mEnter Mobile".center(width))
         mobile_number=input("-->")
         print("\033[32mEnter Email".center(width))
         email=input("-->")
         print("\033[32mEnter Address".center(width))
         address=input("-->")
         print("\033[32mEnter Balance".center(width))
         balance=float(input("-->"))
         time_updated=time   
         data={"Account Number":[account_number],
                  "Name":[name],
                  "Mobile Number":[mobile_number],
                  "Email":[email],
                  "Address":[address],
                  "Balance":[balance] ,
                  "Time Updated":[time_updated]
                  }
            
         dataframe=pd.DataFrame(data)
         

         dataframe.to_pickle("Customer_Data.pkl")  
         print("\033[36mAccount Created Successfully.\n".center(width))    
         print("\033[32m Press Enter Key To Continue.".center(width))
         to_continue=input()


   def update_account(self):
      
      if os.path.exists("Customer_Data.pkl"):
         print(("\033[32mEnter Account Number:".center(width)))
         account_number=int(input("-->"))
         customer_data=pd.read_pickle("Customer_Data.pkl")
         row=customer_data[customer_data['Account Number'] ==account_number]
         if row.empty:
            print("\033[031mSorry The Account You Are Searching To Update Is Not Listed .\n".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
            os.system("cls")
         else:
            print("\033[32mEnter New (Or Old) Mobile".center(width))
            mobile_number=input("-->")
            print("\033[32mEnter New Email (Or Old)".center(width))
            email=input("-->")
            print("\033[32mEnter New Address (Or Old)".center(width))
            address=input("-->")
            print("\033[32mEnter New (Or Old) Balance".center(width))
            balance=float(input("-->"))
            time_updated=time   
         
            index=customer_data[customer_data['Account Number'] == account_number].index[0]
            customer_data.loc[index,["Mobile Number","Email","Address","Balance","Time Updated"]] =[mobile_number,email,address,balance,time]
            customer_data.to_pickle("Customer_Data.pkl")
            print("\033[36mAccount Updated Successfully.\n".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
            os.system("cls")
      
      else:
         print("\033[31mNo Pre-Data Exists To Update.".center(width)) 
         print("\033[32m Press Enter Key To Continue.".center(width))
         to_continue=input()
         os.system("cls")
      
        
           
   def view_account(self):
      if os.path.exists("Customer_Data.pkl"):
         data=pd.read_pickle("Customer_Data.pkl")
         print(("\033[32mEnter Account Number:\033[35m".center(width)))
         account_number=int(input("-->"))
         row=data[data['Account Number'] == account_number]
         if row.empty:
            print("\033[031mSorry The Account You Are Searching For Is Not Listed Yet .\n".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
         else:
            print(row)
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
               
      else:
          print("\033[31mNo Pre-Data Exists To View.".center(width))  
          print("\033[32m Press Enter Key To Continue.".center(width))
          to_continue=input()

   def view_data(self):
      if os.path.exists("Customer_Data.pkl"):
         data=pd.read_pickle("Customer_Data.pkl")  
         if data.empty:
            print("\033[031mSorry No Data Exist To View.\n".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
         else:
            print("\033[35m",data)
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
      else:
         print("\033[31mNo Pre-Data Exists To View.\n".center(width)) 
         print("\033[32m Press Enter Key To Continue.".center(width))
         to_continue=input()
            
   def delete_account(self):
      if os.path.exists("Customer_Data.pkl"):
         data=pd.read_pickle("Customer_Data.pkl")
         print(("\033[32mEnter Account Number:".center(width)))
         account_number=int(input("-->"))
         row=data[data['Account Number'] == account_number]
         if row.empty:
            print("\033[031mSorry The Account You Are Searching To Delete Is Not Listed .\n".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()
         else:   

            data=data.drop(data[data['Account Number'] == account_number].index)
            data.to_pickle("Customer_Data.pkl")
            print("\033[36mAccount Deleted Successfully.".center(width))
            print("\033[32m Press Enter Key To Continue.".center(width))
            to_continue=input()

      else:
          print("\033[31mNo Pre-Data Exists To Delete.\n".center(width)) 
          print("\033[32m Press Enter Key To Continue.".center(width))
          to_continue=input()     
       
      
cond=True
while cond==True:
    os.system("cls")
    print("""\033[36mSystem Function:""".center(width) )
    print("\033[34m(1)Make An Admin Account:".center(width+3))
    print("""(2)Log In To Admin Account: """.center(width))
    print("(3)Close The Program:\t".center(width-5))
    opt=int(input("-->"))
    
    if opt == 1:
      admin_account_exist=os.path.exists('super_admin.bat')
      if admin_account_exist :
         os.system("cls")
         print("\033[31mAn Admin Accounts Already Exists, Please Login To Admin Account".center(width))
         print("\033[32mPress Enter Key To Continue.".center(width))
         to_continue=input()
      else:
         os.system("cls")
         print("\033[32mPlease Enter Your Name".center(width))
         admin_name=input("-->")
         os.system("cls")
         print("""\033[31mYour Passwds Must Contain A Capital, A Small, A Number, And A Symbol
With Minimum Length Of 16 Character""".center(width))
         admin_password=get_password()
         
         admin_details=str((bin(int((admin_name).encode("utf-8").hex(),16)))[2:])+ "null"+str((bin(int((admin_password).encode("utf-8").hex(),16)))[2:])
         with open("super_admin.bat","wb") as f:
            pickle.dump(admin_details,f)
    elif opt == 2:
      admin_account_exist='super_admin.bat'
      if admin_account_exist in os.listdir():
               with open("super_admin.bat",'rb') as f:
                   data=pickle.load(f)
                   os.system("cls")
                   print("\033[32mEnter Your Admin Name:\t".center(width))
                   admin_name=input("-->")
                   print("\033[32mEnter Your Admin Password:\t".center(width))
                   admin_password=getpass.getpass("-->")
                   admin_details=str((bin(int((admin_name).encode("utf-8").hex(),16)))[2:])+ "null"+str((bin(int((admin_password).encode("utf-8").hex(),16)))[2:])
               if admin_details==data:
               
                  manager=MANAGER(admin_name,admin_password)
                  while cond==True:
                     os.system("cls")
                     print("\033[35mAdmin Privileges: ".center(width))
                     print("\033[36m (1) Create Customer Account:".center(width-2))
                     print("\033[36m(2) Update Customer Account:".center(width))
                     print("\033[36m(3) View An Account:".center(width-7))
                     print("\033[36m(4) View Whole Customer Database:".center(width+4))
                     print("\033[36m(5) Delete A Customer Account:".center(width+2))
                     print("\033[36m(6) Close Admin Privileges:".center(width-1))
                     opt2=int(input("-->"))
                     os.system("cls")
                     if opt2==1:
                        manager.add_account()
                     elif opt2==2:
                        manager.update_account()
                     elif opt2==3:
                        manager.view_account()
                     elif opt2==4:
                        manager.view_data()
                     elif opt2==5:
                        manager.delete_account()
                     elif opt2==6:
                        cond=False   
                     else:   
                        print("\033[31mOOPS!!! You Selected An Option That Was Not Listed\033[0m")
               else:
                  print("\033[31mThe Admin Details Entered Were Wrong.".center(width))
                  print("\033[32m Press Enter Key To Continue.".center(width))
                  to_continue=input()
      else:
         print("\033[31m Sorry No Admin Account Already Exist.".center(width))
         print("\033[32mPress Enter Key To Continue:".center(width))
         to_continue=input()
    elif opt== 3:
       print("\033[35mThanks For Using The Program.".center(width))
       print("\033[35mHave A Nice Day ! ! ! \033[0m".center(width-2))
       cond=False
    else:
       print("\033[31mOOPS!!! You Selected An Option That Was Not Listed\033[0m")




