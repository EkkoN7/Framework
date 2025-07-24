def user_input_validation(user_input):
    if user_input.isalpha() == True:
        return "isalpha"
    elif user_input.isdigit() == True:
        return "isdigit"
    elif user_input.isalnum() == True:
        return "isalnum"
    else:
        return None



def user_password_validation():
    user_pwd = input("Password (12-20 characters required): ").strip()
    if len(user_pwd) <= 20 and len(user_pwd) >= 12:
        return user_pwd
    else:
        return "Please enter a valid password."


