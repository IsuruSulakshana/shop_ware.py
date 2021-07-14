        # -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:58:05 2021

@author: ASUS
"""
D = {}
list_1 = []
list_2 = []

def main():
    global list_1
    global list_2
    
    def number():
        Contact_No = input("3) Contact No:")
        n = str(Contact_No)
        if int(len(n)) == 10:
            pass  
          
        else:
            print(' ')
            print(" Phone Number is Incorrect,Please Check Again.")
            main()  
            
        list_1 = Contact_No       
        list_2.append(list_1)    
    number()
  
def details():
    global D
    global list_2
        
    try:
        G = True
        while(G):
            Name = input("1) Name:")
            Adress = input("2) Adress:")
            main()
            Contact_No = list_2[0]            
            import datetime
            x = datetime.datetime.now()
            Last_Date_of_Arrival = x.year,x.month,x.day
            Arrived_Time = x.hour,x.minute,x.second        
            
            
            
            class Customer:
                def __init__(self,Name,Adress,Contact_No,Last_Date_of_Arrival,Arrived_Time):
                    self.__Name= Name.capitalize()       # priwate
                    self.__Adress = Adress.capitalize()  # private 
                    self.__Contact_No = Contact_No       # private
                    self.Last_Date_of_Arrival = Last_Date_of_Arrival
                    self.Arrived_Time = Arrived_Time
                  
                def private(self):
                    D[C.__Name]= C.__dict__
                
                def hello(self):
                    print("* Hello",C.__Name,"['_']")
                    print("* Thank You for your information,Because of Covid19.")
                    print("* Stay Safe")
                    
                    
            C = Customer(Name,Adress,Contact_No,Last_Date_of_Arrival,Arrived_Time)
            print(" ")
            #print("Hello",C.Name,"['_']")
            #print("Thank You for your information,Because of Covid19.")
            #D[Name.Name]= Name.__dict__
            C.hello()
            C.private()
            list = [1]
            for i in list:
                list_2 = [ ]
            G = False
               
    except:
        pass

def customdetails():
    global D
    print(" ")
    for a,b in D.items():
        print("===========================================")
        print("            =","Customer","Details =")
        print("-------------------------------------------")
        for x,y in b.items():
            print("*", x,":",y)
            print("-------------------------------------------")
            
            
        print("===========================================")
        print(" ") 
        print(" ")
        
    
def raw():
    details()

def raw1():
    global D
    if D == { }:
    	print("No Attendance"+"\n ")
    else:
    	customdetails()
    

if __name__ == "__main__":
    raw()
    raw1()


































