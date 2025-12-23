import re

# Define regex for a simple email pattern
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def check_email(email):
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

# User input
user_input = input("Enter an email address: ")
print(f"{user_input} → {check_email(user_input)}")

# Test cases
emails = ["student@mku.ac.ke", "user123@gmail.com", "bad-email@", "test@domain"]
for e in emails:
    print(f"{e} → {check_email(e)}")
