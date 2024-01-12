password = input("please enter a password: ")
password =password.replace(' ',"")
if len(password)>=8:
    print("password accepted")
else:
    print("password not lonnger than 8 characters")