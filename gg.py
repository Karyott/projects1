import os
clear = lambda : os.system("clear")
clear()


setA = {"1","2","3","4"}
setB = {"3","4","5","6"}

while True:
  print ("Option A")
  print ("A.Input set A :")
  print ("B.Input set B :")
  print ("C.Next Option")
  print ("Q.Quit")
 
  x = input("Select an Option:")

  if x == "A":
     clear()
     print ("Input Set A")
     n = input("Please input here :")
     clear()
    
     if n in setA:
        clear()
        print ("\nAlready Found in Set A")
        input("Please Enter to Continue...")  
        clear()

     else:
        clear()
        setA.add(n)
        print (f"Set A : {setA}")
        
  if x == "B":
    clear()
    print ("Input Set B")
    n = input("Please input here :")
    clear()
    
    if n in setB:
       clear()
       print ("\nAlready Found in Set A")
       input("Please Enter to Continue...")  
       clear()

    else:
       clear()
       setB.add(n)
       print (f"Set B : {setB}")

  if x == "C":
    clear()
    print ("Proceed to the next option? :")
    n = input ("Y or N? :")        
    clear()
    
    if n == "N":
      clear()
      input ("Please Enter to Continue...")
      
    
    else : break

  if x == "Q":
    clear()
    print ("Do you want to Quit? :")
    n = input ("Y or N? :")        
    clear()
    
    if n == "N":
      clear()
      input ("Please Enter to Continue...")
      
    
    else:
      clear()
      print("babyeee...")
      quit()
      clear()

  while True:
    print ("Option B")
    
    print ("A : A UNION B")
    print ("B : A INTERSECT B")
    print ("C : A MINUS B")
    print ("Q : Back to Menu")
    
    x = input("Enter an Option:")
    
    if x == "A":
      clear()
      setA.union(setB)
      print (f"A UNION B : {setA}")
      
    if x == "B":
      clear()
      setA.intersect(setB)
      print (f"A INTERSECT B : {setB}")
    
    if x == "C":
      clear()
      setA.remove(setB)
      print (f"A MINUS B : {setA}")
    
    if x == "Q":
      clear()
      print ("Do you want to Back to Menu? :")
      n = input ("Y or N? :")        
      clear()
    
    if n == "N":
      clear()
      input ("Please Enter to Continue...")
      
    
    else:
      exit()
      
      
              
            
            
            
  
            
            
            
            
            
            
                             
     