password=input("Enter your Password:")

length=len(password)

if length < 4:
    print("The password is weak")
elif length >=4 and length < 8:
    print("The password is medium")
else:
    print("The password is strong")

    if "@" in password or "#" in password or "$" in password:
        print("The password contains special characters")
    else:
        print("Add special characters for better security")