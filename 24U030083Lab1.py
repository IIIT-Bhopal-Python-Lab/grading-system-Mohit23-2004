a=int(input("Enter marks:"))
if(a>=90 and a<=100):
    print("A")
elif(a>=75 and a<=89):
    print("B")
elif(a>=60 and a<=74):
    print("C")
elif(a>=40 and a<=59):
    print("D")
elif(a<=40):
    print("F")
else:
    print("Invalid input")