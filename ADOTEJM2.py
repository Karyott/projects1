#lab 0.2

#submitted by John Mark S. Adote

#Counting backward While Statement



print("enter an integer")

n=int(input())

f=n

if n<0:

  print("invalid input")



elif n==0:

    f+=1

    print("the factorial of",n,"is",f)



    

else:

    i=n

    while i>1:

            i-=1

            f*=i



    print("the factorial of",n,"is",f)



    

