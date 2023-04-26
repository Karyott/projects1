import os
clear = lambda: os.system("clear")


setA = {"1","2","3","4","5","6"}
setB = {"2","4","6","8","10"}
setC = {""}
setU = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20",}
setA.clear()
setB.clear()
setC.clear()
disname = "Uni"

while True:
    clear()

    print("Nested Menu")
    
    print("1 : I/O")
    print("2 : Operations")
    print("3 : Display")
    print("Q : Quit")

    selection = input("\nSelect an Option : ")

    if selection == "1":
        while True:
            clear()

            print("I/O Menu\n")

            print("1 : Input Set A")
            print("2 : Input Set B")
            print("Q : Back to main menu")

            selection1 = input("\nSelect an Option : ")

            if selection1 == "1":
                while True:
                    clear()

                    print("Input Set A")
                    print("\n[ADDITIONAL OPTIONS]\nclear : remove all items from set\nremove : remove specific item from set\n")

                    if len(setA) >= 1:
                        print(setA)

                    additm = input("\nEnter Item Name for Set A (Type done to finish): ")

                    if additm == "clear":
                        if len(setA) >= 1:
                            while True:
                                clear()

                                print("Remove all items from set A")

                                notif = input("Are you sure you want to remove all items from set A? (Y|N): ")

                                if notif == "Y":
                                    setA.clear()
                                    break

                                elif notif == "N":
                                    break

                                else:
                                    clear()

                        else:
                            clear()
                            input("Set A is already empty")
                        
                    elif additm == "remove":
                        if len(setA) >= 1:
                            while True:
                                clear()

                                print("Remove Item from Set\n")

                                print(setA)

                                delitm = input("\nEnter an item name you want to remove from set A (Type done to finish): ")

                                if delitm == "":
                                    clear()

                                elif delitm in setA:
                                    setA.discard(delitm)

                                elif delitm == "done":
                                    break

                                else:
                                    clear()
                                    input("\nCan't remove item. Item not found...")

                        else:
                            clear()
                            input("Set A is empty")

                    elif additm == "done":
                        break

                    elif additm == "":
                        clear()

                    elif additm in setA:
                        clear()
                        input("Can't add item. Item already in the set A...")

                    elif additm not in setA:
                        if additm not in setU:
                            clear()
                            input("Item not found in Universal Set...")

                        elif additm in setU:
                            setA.add(additm)

            if selection1 == "2":
                while True:
                    clear()

                    print("Input Set B")
                    print("\n[ADDITIONAL OPTIONS]\nclear : remove all items from set\nremove : remove specific item from set\n")

                    if len(setB) >= 1:
                        print(setB)

                    additm = input("\nEnter Item Name for Set B (Type done to finish): ")

                    if additm == "clear":
                        if len(setB) >= 1:
                            while True:
                                clear()

                                print("Remove all items from set B")

                                notif = input("Are you sure you want to remove all items from set B? (Y|N): ")

                                if notif == "Y":
                                    setB.clear()
                                    break

                                elif notif == "N":
                                    break

                                else:
                                    clear()

                        else:
                            clear()
                            input("Set B is already empty")
                        
                    elif additm == "remove":
                        if len(setB) >= 1:
                            while True:
                                clear()

                                print("Remove Item from Set\n")

                                print(setB)

                                delitm = input("\nEnter an item name you want to remove from set B (Type done to finish): ")

                                if delitm == "":
                                    clear()

                                elif delitm in setA:
                                    setA.discard(delitm)

                                elif delitm == "done":
                                    break

                                else:
                                    clear()
                                    input("\nCan't remove item. Item not found...")

                        else:
                            clear()
                            input("Set B is empty")

                    elif additm == "done":
                        break

                    elif additm == "":
                        clear()

                    elif additm in setB:
                        clear()
                        input("Can't add item. Item already in the set B...")

                    elif additm not in setB:
                        setB.add(additm)

                    elif additm not in setB:
                        if additm not in setU:
                            clear()
                            input("Item not found in Universal Set...")

                        elif additm in setU:
                            setB.add(additm)

            if selection1 == "Q":
                break

    elif selection == "2":
        if len(setA) and len(setB) >= 1:
            while True:
                clear()

                print("Operations\n")

                print("1 : A Union B")
                print("2 : A Intersect B")
                print("3 : A - B")
                print("Q : Back to main menu")

                selection2 = input("\nSelect an Option : ")

                if selection2 == "1":
                    disname = "A Union B"
                    if len(setA) and len(setB) >= 1:
                        setC = setA.union(setB)
                        break

                    else:
                        input("Must enter Set A/B values first to continue...")
                        break

                if selection2 == "2":
                    disname = "A Intersection B"
                    if len(setA) and len(setB) >= 1:
                        setC = setA.intersection(setB)
                        break

                    else:
                        input("Must enter Set A/B values first to continue...")
                        break

                if selection2 == "3":
                    disname = "A - B"
                    if len(setA) and len(setB) >= 1:
                        setC = setA.difference(setB)
                        break

                    else:
                        input("Must enter Set A/B values first to continue...")
                        break

                if selection2 == "Q":
                    break

        else:
            clear()
            input("Must enter Set A/B values first to continue...")

    elif selection == "3":
        clear()

        print("1 : Display Set C")
        print("2 : Display Universal Set")
        print("Q : Back to main menu")

        selection4 = input("\nSelect an Option : ")
        while True:
            if selection4 == "1":
                clear()
                if len(setC) >= 1:
                    print(disname)
                    n = 1
                    while n <= len(setC):
                        n = 1
                        print("\nSet C list:")
                        for x in setC:
                            print("("+str(n)+") - "+str(x))
                            n = n+1 

                else:
                    clear()
                    input("Must do operation first to continue...")
                    break

                input("\nPress enter to continue...")
                break

            elif selection4 == "2":
                clear()
                n = 1
                while n <= len(setU):
                    n = 1
                    print("Universal Set list:")
                    for x in setU:
                        print("("+str(n)+") - "+str(x))
                        n = n+1

                input("\nPress enter to continue...")
                break

            elif selection4 == "Q":
                break

            else:
                clear()

        

    elif selection == "Q":
        while True:
            clear()

            selection3 = input("Are you sure you want to quit? (Y|N): ")

            if selection3 == "Y":
                print("Bye Bye...")
                quit()

            elif selection3 == "N":
                break