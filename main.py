import string

password = input("Enter a Password: ")

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
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print(f"Password strength: {strength}")