import secrets
import string

def generate_password(length=12, complexity="medium"):
    # Define character sets based on complexity
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation
    else:
        raise ValueError("Invalid complexity level")

    # Generate password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    # Get user input
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter complexity level (low/medium/high): ")

    # Generate and display password
    password = generate_password(length, complexity)
    print("Generated Password:", password)

main()
