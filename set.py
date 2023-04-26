import os
clear = lambda : os.system ("clear")
clear()

subjs = {"Math"}

while True:

    print("My Subjects\n")

    print("A : Add subject")
    print("B : Remove subject")
    print("C : Count subject")
    print("D : Search subject")
    print("E : List subject")
    print("Q : Quit")

    selection = input("\nEnter your Option : ")

    if selection == "A":
        clear()
        print("You selected A")
        NS = input("Add new subject here : ")
        clear()

        if NS in subjs:
            clear()
            print("\nElement already in the set")
            input("Press enter to contiunue...")

        else:
            clear()
            subjs.add(NS)
            print(subjs)
            input("Press enter to contiunue...")

    if selection == "B":
        clear()
        print("You selected B")
        NS = input("Remove subject here : ")
        if NS in subjs:
            clear()
            subjs.remove(NS)
            print(subjs)
            input("Press enter to contiunue...")

        else:
            clear()
            print("\nElement not found")
            input("Press enter to contiunue...")

    if selection == "C":
        clear()
        print("You selected C")
        print("the total of items in the set is",len(subjs))
        input("Press enter to contiunue...")

    if selection == "D":
        clear()
        print("You selected C")
        NS = input("search subject here : ")
        clear()

        if NS in subjs:
            clear()
            print("\nsubject found in the set")
            input("Press enter to contiunue...")

        else:
            clear()
            print("\nsubject not found in the set")
            input("Press enter to contiunue...")

    if selection == "E":
        clear()
        print("List of Items\n")
        print(subjs)
        input("Press enter to contiunue...")
        clear()

    if selection == "Q":
        clear()
        print("Bye...")
        quit()
        
    clear()