#mypassword with digits num
#submitted by John Mark S. Adote
#BSCOE

pw=input('enter password:')
pwlength=len(pw)
if (pwlength<10):
   print('Invalid!!You need at least 10 characters')
UcaseOk=False
LcaseOk=False
NumOk=False
for testchar in pw:
    asciival=ord(testchar)
    if (asciival>=97) and (asciival<=122):
     LcaseOk=True  
    elif (asciival>=65) and (asciival<=90):
     UcaseOk==True
    elif(asciival>=48) and (asciival<=57):
     NumOk=True
     
if (LcaseOk==False):
 print('Invalid!!You need at least 1 lower case letter')
elif (UcaseOk:=False):
 print('Invalid!!You need at least 1 upper case letter')
elif (NumOk==False):
 print('Invalid!!You need at least 1 number')
else:
    print('WOW!your password is ok')
      
