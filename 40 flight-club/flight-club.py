import requests

CREATOR_NAME = "YOUR NAME"
SHEETY_USERS_ENDPOINT = "YOUR SHEETY USERS ENDPOINT"
SHETTY_HEADER = {
    "Authorization": "Bearer YOUR TOKEN"
}

print(f"Welcome to {CREATOR_NAME}'s Flight Club.\n"
      f"We find the best flight deals and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
check_email = input("Type your email again.\n")

while email != check_email:
    print("Emails do not match.")
    email = input("What is your email?\n")
    check_email = input("Type your email again.\n")
print("You're in the club!")

body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}

response = requests.post(
    url=SHEETY_USERS_ENDPOINT,
    json=body,
    headers=SHETTY_HEADER,
)
print(response.text)
