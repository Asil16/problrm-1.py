#username
def get_username():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("Username should not be empty. Please try again.")
        elif len(username) > 50:
            print("Username should not exceed 50 characters. Please try again.")
        else:
            print(f"Username '{username}' is valid!")
            break

get_username()

#Password

import re

def is_valid_password(password):
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
   
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special symbol."
    

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    
  
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return False, "Password must contain both uppercase and lowercase characters."
    

    return True, "Password is valid."

def main():
    password = input("Enter your password: ")
    is_valid, message = is_valid_password(password)
    if is_valid:
        print(message)
    else:
        print("Invalid password:", message)

if __name__ == "__main__":
    main()

#email
import re

def is_valid_email(email):
    # Define the regular expression for the email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the regular expression
    if re.match(email_regex, email):
        return True, "Email is valid."
    else:
        return False, "Invalid email address. Please ensure it meets the following criteria:\n" \
                      "1. The email should have '@' symbol.\n" \
                      "2. It should have alphanumeric characters before and after the '@' symbol.\n" \
                      "3. After the '@' symbol, it should have letters having '.' character in between."

def main():
    email = input("Enter your email address: ")
    is_valid, message = is_valid_email(email)
    if is_valid:
        print(message)
    else:
        print(message)

if __name__ == "__main__":
    main()


