import re
import sys

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Determine the strength based on criteria met
    if criteria_met < 3:
        return "Weak"
    elif criteria_met == 3 or criteria_met == 4:
        return "Moderate"
    else:
        return "Strong"


if __name__ == "__main__":
    # Check if exactly two arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <password>")
    else:
        try:
            password = sys.argv[1]
            strength = check_password_strength(password)
            print(f"The password strength is: {strength}")
        except ValueError:
            print("Please provide a valid password string.")

