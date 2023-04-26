#Programming Exam
#submitted by John Mark S. Adote
#BSCOE I

h=float(input('Enter Your Feet'))
i=float(input('Enter your Inch'))
w=float(input('Enter your Weight'))
h=((h*12)+i)*(2.54)/100

bmi=w/(h*h)
print('your body mass index is',bmi)
	
if bmi<=18.5:
    print('underweight')
elif bmi<=24.9:
    print('normal weight'')
elif bmi<=29.9:
    print('oversize!')
else:
    print('obese')
