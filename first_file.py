1# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:54:50 2021

@author: ASUS
"""   
data={"apple": 30,"banana": 60,"orange": 50,"mango" : 40,"pine_apple":70}

total={"apple": 0,"banana": 0,"orange": 0,"mango":0,"pine_apple":0}

dict_1={"apple": 0,"banana": 0,"orange": 0,"mango":0,"pine_apple":0}

dict_2={"apple": 0,"banana": 0,"orange": 0,"mango":0,"pine_apple":0}

list_1 = [ ]


          
def sellermethod3():
    global data
    global total
    global dict_1
    global dict_2
    global list_1
    
    
    try:
        while(True):
            i , v = input().split()
            if str(i) in data:
                dict_1.update({str(i):0})
                dict_2.update({str(i):0})
            #print(total)
            #print(dict_1)
            #print(dict_2)
                total[i] = total[i] + int(v)*data[i]
                dict_1[i] = dict_1[i] + int(v)*data[i]
                dict_2[i] = dict_2[i] + int(v)
                pass
            else:
                print("Wrong Item")
                #sellermethod3()
                
    except:
        pass
    #print(total)
    #print(dict_1)
    #print(dict_2)
    
    def test():
        global dict_2
        global dict_1
        global list_1
        for x,y in dict_1.items():
            for m in dict_2.values():
                if y == 0 and m == 0:
                    continue
                elif y > 0 and dict_2[x] == m and m > 0:
                    print("|",x,"|",m,"|",y,"|")
                    print("+=============================================================+")
                    print("|                                                             |")
                    list_1.append(x)
                    break 
  
    def test_1():
        global list_1
        print("Total :","Rs",bill)
        print("To Print Bill")
        money = str(input("Enter paid amount:"))
        print(" ")
        print("+=============================================================+")
        f = open("photo_file.txt", "r")
        print(f.read())
        #print("+=============================================================+")
        #print("|                                                             |")
        #print("|                          FG shop                            ")
        #print("|                                                             |")
        #print("+=====================+==================+====================+")
        print("|                     |                  |                    |")
        import datetime
        x = datetime.datetime.now()
        print("| Date:",x.year,"-",x.month,"-",x.day,"                      Time:", x.hour,"-",x.minute,"-",x.second)
        print("|                     |                  |                    |")
        print("+=====================+==================+====================+")
        print("|                     |                  |                    |")
        print("| Name                | Quantity         | Price              ")
        print("|                     |                  |                    |")
        print("+=====================+==================+====================+")
        print("|                                                             |")
        test()
        print("| Total :", "Rs",bill,"                                             ")
        print("|                                                             |")
        print("+=============================================================+")
        print("|                                                             |")
        print("| Balance :", "Rs",(int(money)-bill),"                                           ")
        print("|                                                             |")
        print("+=============================================================+")
        print("|                                                             |")
        print("| Number Of Items:","|",len(list_1),"|")
        print("|                                                             |")
        print("+=============================================================+")
        print("|                                                             |")
        print("|                  Thank You.Come Again !                     ")
        print("|                                                             |")
        print("+=============================================================+")            
        print("+=============================================================+")  
        
        for i in list_1:
            list_1 = []
        
        
    bill=0
    for i ,v in total.items():
        bill=bill+ v
        total.update({str(i):0})
    test_1()
    
    
    
    for i ,v in total.items():        
        dict_1.update({str(i):0})
        dict_2.update({str(i):0})
               
        
def sellermethod6():
    
    global data
    global total
    
    try:
        while(True):
            x , y = input().split()
            if str(x) not in data:
                   data[str(x)] = int(y)
                   total[str(x)] = int(0)
                   print("####-------------------New Item added Sucsess----------- --####")
                   print("Press Enter")
                   pass
            elif str(x) in data:
            	    print(str(x),"is in the price list")
            	    print(" ")
            	    pass
            	    
            	    
            	    
            	    
            	    
            
    except:
        pass
    
def sellermethod8():
       
    global data
    global total
    
    try:
        while(True):
           
            x , y = input().split()
            if str(x) in data:
                data[str(x)] = int(y)
                total[str(x)] = int(0)
                print("####--------------New Quantity Update Sucsess--------------####")
                print("Press Enter")
                pass
            elif str(x) not in data:
                print("No such Item.Read the Price List again")
                print("")
                pass
                   
    except:
        pass

def sellermethod7():
    global data
    print("===============")
    for a , b in data.items():
        print("*" , a , b)
        print("---------------")
    print("===============")
   
        
def sellermethod10():
    global data
    stock = str(input("Enter number:"))
    print("")    
    if str(stock) == "1":
        print("===============")
        
        for a,b in data.items():
            print("*" , a)
            print("---------------")
        print("===============")    
    elif str(stock) == "2":
        print("===============")
        for a,b in data.items():
            print("*" , a , b)
            print("---------------")
        print("===============")    

        
def main4():
    sellermethod10()
        
def main3():
    sellermethod8()

def main2():
    sellermethod7()
   
def main1():
    sellermethod6()     

def main():
    sellermethod3()
     
if __name__ == "__main__":
    
    main()
    main1()
    main2()
    main3()
    main4()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
