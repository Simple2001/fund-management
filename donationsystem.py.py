import os
import fileinput


def dotate(data,f_donar,f_amount):
    f_donar.append(input("type the name of the donor :"))
    f_amount.append(int(input("whats the amount :")))
    data.write(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1])+"\n")
    print("ID is :",(len(f_amount)-1))
    return(data,f_donar,f_amount)
def retrive(data,f_donar,f_amount):
    print("type the ID of the donation:")
    b=int(input())
    if (b<len(f_amount)):
        print("NAME:",f_donar[b])
        print("AMOUNT:",f_amount[b])
    else:
        print("invalid ID")
def adddata(data,f_donar,f_amount):
    print("type the ID:")
    b=int(input())
    if (b<len(f_amount)):
        print("type the amount :")
        c=int(input())
        for line in fileinput.input(data):
            line=line.replace(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1]),str(f_donar[len(f_amount)-1]+c)+" : "+ str(f_amount[len(f_amount)-1]))
        f_amount[b]=f_amount[b]+c
    else:
        print("invalid ID")
def retriveall(data,f_donar,f_amount):
    for i in data:
        print(i)
if( __name__ == "__main__"):
    os.chdir("C:\\Users\\saran\\New folder")
    data=open("Data.txt",'a+')
    print(" press 1 for admin \n press 2 for user : ")
    f_amount=[]
    f_donar=[]
    key=int(input())
    if(key==1):
        passcode='IIITDWD'
        print("Enter the Passcode :")
        p=input()
        if(p==passcode):
            print(f" press 1 to donate \n press 2 to get data \n press 3 to add amount \n press 4 to get all the info. \n press 5 to terminate the process")
            while(1):
                comand=int(input())
                if(comand==1):
                    dotate(data,f_donar,f_amount)
                elif(comand==2):
                    retrive(data,f_donar,f_amount)
                elif(comand==3):
                    adddata(data,f_donar,f_amount)
                elif(comand==4):
                    retriveall(data,f_donar,f_amount)
                else:
                    break
        else:
            print("this is not the correct password")
    elif(key==2):
        print(f" press 1 to donate\n press 2 to get the data of donation \n press 3 to add amount \n press 4 to get all the data \n press 5 to terminate the process")
        while(1):
            comand=int(input())
            if(comand==1):
                dotate(data,f_donar,f_amount)
            elif(comand==2):
                retrive(data,f_donar,f_amount)
            elif(comand==3):
                adddata(data,f_donar,f_amount)
            else:
                break