medical_cause = input("do you have any medical cause Y or N :")
attendance =int(input("enter your student attendence:"))
if medical_cause == "Y":
    print ("you are allowed")
else:
    if attendance>=75:
        print ("allowed")
    else:
        print("not allowed")
