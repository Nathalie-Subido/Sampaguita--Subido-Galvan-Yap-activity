#=======================================================================================================================
#               School Grade Level Validator
#=======================================================================================================================

# Data Type Validator validating if grade level is a whole number

accepted_grade_levels = [7,8,9,10,11,12]
try:
    grade_level = int(input("Please enter grade level: "))
    # Validating the range of grade level
    if grade_level in accepted_grade_levels:
        print("Valid Grade Level")
    else:
        print("Invalid Grade Level")
# Data Type Validator displaying wrong data type
except ValueError:
    print("Invalid Grade Level. Please enter a whole number")
