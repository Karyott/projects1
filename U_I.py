import os
clear = lambda : os.system ("clear")
clear()

sA = {"1,2,3"}
SB = {"3,4,5"}
while True:

    print("My Subjects\n")

    print("A - Input Set A:")
    print("B - Input Set B:")
    print("Q - Quit")

    n = input("\nEnter your Option : ")

    if n == "A":
         clear()
         print("Please Input Set A:")
         s = input("Input a Set A here : ")
         clear()

         if s in sA:
              clear()
              print("\nThe numbers already in the set")
              input("Press enter to contiunue...")

         else:
             clear()
             sA.add(s)
             print(sA)
             input("Press enter to contiunue...")

    if n == "B":
         clear()
         print("Please Input Set B:")
         s = input("Input a Set A here : ")
         clear()

         if s in sA:
             clear()
             print("\nThe numbers already in the set")
             input("Press enter to contiunue...")

         else:
            clear()
            sA.add(s)
            print(sA)
            input("Press enter to contiunue...")

    if n == "Q":
        clear()
        print("Do you want to Quit?")
        a = input ("Y or N?")
        clear()
       
        if a == "N":
             clear()
             print("Press Enter to continue")
        else:
            clear()
            print("byee..bye..")
            quit()        
            clear()      