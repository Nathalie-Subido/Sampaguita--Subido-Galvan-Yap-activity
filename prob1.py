#=======================================================================================================================
#                           Student Age Validator
#=======================================================================================================================

# Data Type Validator validating if age is a whole number
try:
    student_age = int(input("Enter your age: "))
    # Validating the range of student age
    if student_age < 0:
        print("Invalid Age. Please enter a whole number. ")

    else:
        if 12 <= student_age <= 18:
            print("Valid Age.")
        else:
            print("Invalid Age. Age must be from 12 to 18. ")
# Data Type Validator displaying wrong data type
except ValueError:
    print("Invalid Age. Please enter a whole number. ")
