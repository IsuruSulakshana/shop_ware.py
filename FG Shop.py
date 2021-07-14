# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:01:35 2021

@author: ASUS
"""

while(True):
 
 f = open("shop_name.txt", "r")
 print(f.read())
     
 def sellermethod8():
     print("")
     print("Enter Number to access to system")
     print("Systems")
     print("------------------------------------------")
     print(" 1) Type 1: Enter to seller managment")
     print("------------------------------------------")
     print(" 2) Type 2: Enter to customer managment")
     print("------------------------------------------")
     print(" 3) Type 0: shutdown system")
     print("------------------------------------------")
     print(" ")  
  
 import first_file , second_file

 def sellermethod1(num_B):
     if str(num_B) == "1": 
         print(" ")
         print(" ")
         print("Available products and Unit Price per kilo(Rs)")
         first_file.main2()
         print("####------------------Create New Bill----------------------####")
         print("Enter : Product_Name_Ordered_Quantity")
         print("Enter : $ to get Total")
         print(" ")
         first_file.main()
         print(" ")
         sellermethod4()
        
     elif str(num_B) == "2":
         print(" ")
         print(" ")
         print("####------------------Add New Item-------------####")
         print("Enter New Item Name and Unit Price per kilo(Rs): ")
         print("Eg:- mango 100")
         print(" ")
         first_file.main1()
         print(" ")
         print('Updated Price List')
         first_file.main2()
         print(" ")
         sellermethod4()
         
         
     elif str(num_B) == "3":
         print(" ")
         print(" ")
         print("PRICE LIST")
         first_file.main2()
         print("####-------Type ITEM and NEW QUANTITY-----------####")
         print("Eg:- mango 100")
         print(" ")
         first_file.main3()
         
         print(" ")
         print("Updated Price List")
         first_file.main2()
         print(" ")
         sellermethod4()
         
     elif str(num_B) == "4":
         print(" ")
         print(" ")
         print("NOW STOCK")
         print(" 1) Type 1: Stock Items")
         print(" 2) Type 2: Stock Items and Unit price per kilo(Rs)")
         print(" ")
         first_file.main4()
         
         print(" ")
         sellermethod4()
         
     elif str(num_B) == "0":
         sellermethod8() 
         sellermethod5()  
         pass
     else:
         print("####-----------Wrong Type,please Re Type Number------------####")
         print(" ")
         sellermethod4()
         pass
     
        
     
 def customermethod_1(num_C):
     if str(num_C) == "1":
         print(" ")
         second_file.raw()
         print(" ")
         customermethod_0()
         
     elif str(num_C) == "2":
         print(" ")
         print("Available Items and Unit Price per kilo(Rs) ")
         first_file.main2()
         print(" ")
         customermethod_0()
         
         
     elif str(num_C) == "3":
         print(" ")
         print("Available Items and Unit Price per kilo(Rs)")
         first_file.main2()
         print("####---------------------Buy Items-------------------------####")
         print("Enter : Product_Name_Ordered_Quantity")
         print("Enter : $ to get Total")
         print(" ")
         first_file.main()
         print(" ")
         customermethod_0()
         
     elif str(num_C) == "4":
         print(" ")
         print("Passwrd = 5319889")
         password = str(input("Type Password:"))
         
         if str(password) == "5319889":
             second_file.raw1()
             customermethod_0()
         else:
             print("Wrong Password")
             print(" ")
             customermethod_0()
             
         
     elif str(num_C) == "0":
         sellermethod8() 
         sellermethod5()  
         pass
     else:
         print("####-----------Wrong Type,please Re Type Number------------####")
         print(" ")
         customermethod_0()
         pass    
         
     
 def customermethod_0():
     print("Enter Number to access to system")
     print("Customer Tasks")
     print("------------------------------------------")
     print(" 1) Type 1: Attendance for Covid situation")
     print("------------------------------------------")
     print(" 1) Type 2: Show Available Items")
     print("------------------------------------------")
     print(" 2) Type 3: Buy Items")
     print("------------------------------------------")
     print(" 3) Type 4: See All Attendance")
     print("------------------------------------------")
     print(" 4) Type 0: Go Back")
     print("------------------------------------------")
     print(" ")
     num_C = str(input("Enter Number:"))
     customermethod_1(num_C)
     
 def sellermethod4():
     print("Enter Number to access to system")  
     print("Sellor Tasks")
     print("------------------------------------------")
     print(" 1) Type 1: Create new bill")
     print("------------------------------------------")
     print(" 2) Type 2: Add new item")
     print("------------------------------------------")
     print(" 3) Type 3: Update Quantity")
     print("------------------------------------------")
     print(" 4) Type 4: Show Stock")
     print("------------------------------------------")
     print(" 5) Type 0: Go Back")
     print("------------------------------------------")
     print(" ")
     num_B = str(input("Enter Number:")) 
     sellermethod1(num_B)

 def sellermethod5():
     num_A = str(input("Enter Number:"))
     
     if str(num_A) == "1":
         print("")
         print("===============================================================")
         print("####-----------------Welcome Sellor Section----------------####")
         print("===============================================================")
         print("")
         sellermethod4()
     
     elif str(num_A) == "2":
         print("")
         print("===============================================================")
         print("####---------------Welcome Customer Section----------------####")
         print("===============================================================")        
         print("")
         customermethod_0()
    
     elif str(num_A) == "0":
         sellermethod8() 
         sellermethod5()  
         pass
    
     else:
         print("####-----------Wrong Type,please Re Type Number------------####")
         print("")
         sellermethod8() 
         sellermethod5()  
         pass
     
 sellermethod8() 
 sellermethod5()  
