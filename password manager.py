#import numpy as np
#import random as rand

#login

f = open("usrcredentials.txt","w+")
contchoice = "y"
while(contchoice == "y"):
     usrname = input("enter username: ")
     password = input("enter password: ")
     choice = input("do you want want conform password (y/n)")
     if(choice == "y"):
        login2 = input("enter your entered password: ")
        if(login2 == password):
          print("the username and password are conformed")
          break
        else:
          print("not confirmed")
          break

     if(choice == "n"):
        print("the password is not confirmed")
        contchoice = input("do you want to renter your credentials?(y/n)")
        if(contchoice == "y"):
            continue
        if(contchoice == "n"):
            break

f.write("password: " + password)
f.write(", username: " + usrname)
f.close()

#what i've learnt:
#how to read, write and create files


