# Given a string, check if it only contains digits.

def is_digit(input_str):
    try:
        # If its possible to convert to a number, return True.
        int(input_str)
        return True
    except ValueError:
        # If the string contains letters, above will fail, returning False.
        return False

result = is_digit("095357973590759530")
print(result)  # True

result = is_digit("1234abc567")
print(result)  # False
