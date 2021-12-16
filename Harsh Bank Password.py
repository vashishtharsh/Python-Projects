while True: 
   print('Welcome to SAITM Bank')
   print('1.Withdraw Money')
   print('2.Update Password')
   print('3.Exit')
   user =(input("Enter option: "))
   if (user == "1"):
          user1 =(input("How much you wanto withdraw? "))
          print('Please wait while Your transaction is being Proceed')
          print('Please Collect your Money', user1)
          user1 =(input("Do you want to see your total balance (y/n):"))
          if (user1 == "y"):
                   print("3400000 is balance")
   else:
                   print("Thank You")

  elif (user == "2"):
     pass1 =(input("Enter your Current Password: "))
     if (pass1 == "2552"):
                 pass2=input("Enter your New Password: ")
                 pass2=input("Enter your New Password Again: ")
                 print("Password Updated")
                 user2=input("Do you want to see your Password: y/n")
                 if (user2 == "y"):
                     print("Your NewPassword is :", pass2)
                 else:
                     print("Thank you")
        else:
                 print("Your Password do not match")
  elif (user == "3"):
        print("Thank you")
