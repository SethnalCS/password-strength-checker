import string

def check_password_strength(password):

    score = 0

    # Filters for password strength
    if len(password) >= 8:
        score += 1  
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    # Strength check based on filter scores
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"
    
def feedback(password):
    suggestions = []
    # Check for missing security in password
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not any(char.isupper() for char in password):
        suggestions.append("Add uppercase letters")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include numbers")
    if not any(char in string.punctuation for char in password):
        suggestions.append("Use special characters")

    return suggestions    


password = input("Enter a Password: ")
strength = check_password_strength(password)
suggestions = feedback(password)

# final output
print(f"Password strength: {strength}")
if strength == "Weak" or strength == "Moderate":
    print(suggestions)