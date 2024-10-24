maths=int(input("enter your marks in maths="))
science=int(input("enter your marks in science="))
english=int(input("enter your marks in english="))
urdu=int(input("enter your marks in urdu="))
sst=int(input("enter your marks in pak studies="))
mark=maths+science+english+urdu+sst
avg=mark/5
if avg>90:
    print("grade A")
elif avg<90 and avg>80:
    print("grade B")
elif avg<80 and avg>70:
    print("grade C")
elif avg<70 and avg>60:
    print("grade D")
else:
    print("your a failure")