def userLogin(user_name,password):
    if user_name=="yashu" and password=="1234":
        return True
    else:
        raise Exception("User Name & Password not matched")#User defined Exception
user_name=input("Enter User Name:")
password=input("Enter password:")
result=userLogin(user_name,password)
if result==True:
    print("Logged In succesfully")
else:
    print("User Name or Password is wrong")
