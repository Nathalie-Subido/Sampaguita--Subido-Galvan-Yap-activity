#=======================================================================================================================
#               School Grade Level Validator
#=======================================================================================================================

# Data Type Validator validating if grade level is a whole number

accepted_grade_levels = [7,8,9,10,11,12]
try:
    grade_level = int(input("Please enter grade level: "))
    # Checks if Data type is a whole number
    if grade_level < 0:
        print("Invalid input. Please Enter a whole number")
    else:
        # Validating the range of grade level
        if grade_level in accepted_grade_levels:
            print("Valid Grade Level")
        else:
            print("Invalid Grade Level")
# Data Type Validator displaying wrong data type
except ValueError:
    print("Invalid input. Please enter a numeric value")
