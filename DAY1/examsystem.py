total=int(input("Enter Total Marks:"))

negMarks=int(input("ENTER NEGATIVE MARKS"))
time=int(input("HOW TIME TAKEN"))

if total>=40 and negMarks==0 and time<=3:
    
    print("PASS")

    if total>85:
        print("DISTINCTION")
    elif total>65:
        print("FIRST CLASS")
    elif total>40:
        print("SECOND CLASS")
else:
    print("FAIL")
