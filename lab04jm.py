#Lab.04 
#lec06
#Submitted by Adote John Mark S.
def fact (n):
  f=n
  if n==0:
    f+=1
    return(f)
  else:
    i=n
    while i>1:
            i-=1
            f*=i
    return(f)

    

print ('enter an integer')
num=int(input())
if num<0:
   print("invalid input")
else:
   answer=fact(num)

   print ('the factorial of',num,'is',answer)