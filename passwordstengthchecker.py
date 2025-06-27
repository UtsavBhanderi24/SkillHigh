import re

def check_password_complexity(password):
    # Define regex patterns for different complexity criteria
    patterns = {
        'length': r'.{8,}',        # Minimum 8 characters
        'lowercase': r'[a-z]',     # At least one lowercase letter
        'uppercase': r'[A-Z]',     # At least one uppercase letter
        'digits': r'\d',           # At least one digit
        'special': r'[^a-zA-Z0-9]'  # At least one special character
    }

    # Check each pattern against the password
    for key, pattern in patterns.items():
        if not re.search(pattern, password):
            return False, f"Password does not meet {key} criteria"

    return True, "Password meets complexity criteria"

# Example usage:
password = input("Enter your password: ")
is_complex, message = check_password_complexity(password)
print(message)