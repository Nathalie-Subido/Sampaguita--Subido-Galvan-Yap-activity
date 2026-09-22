#=======================================================================================================================
#                            Username Validator
#=======================================================================================================================

# Enters username
username = input("Enter a username: ")

# Validates if the length and characters of username is valid
if 5 <= len(username) <= 10 and username.isalnum():
    print("Valid username.")
# Not valid
else:
    print("Invalid username.")