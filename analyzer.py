def check_password(password):
    length = len(password)
    score = 0
    print(f"password length: {length}")
    if length < 8:
        print("Password is too short")
    elif length < 12:
        print("good password length")
        score+=20
    else:
        print("strong password length")
        score+=20

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
   
    if has_upper:
        score+=20
    if has_lower:
        score+=20
    if has_digit:
        score+=20
    if has_special:
        score+=20

    print(f"Uppercase: {has_upper}")
    print(f"Lowercase: {has_lower}")
    print(f"Numbers: {has_digit}")
    print(f"Special Characters: {has_special}")
    print(f"score: {score}")

    if score < 40:
       print("Password Strength: Weak")
    elif score < 70:
       print("Password Strength: Medium")
    elif score < 90:
       print("Password Strength: Strong")
    else:
       print("Password Strength: Very Strong")

    print("\nSuggestions:")
    if not has_upper:
        print("-Add at least one uppercase letter.")
    if not has_lower:
        print("-Add at least one lowercase letter.")
    if not has_digit:
        print("-Add at least one number.")
    if not has_special:
        print("-Add at least one special character.")
    if length < 12:
        print("-Use at least 12 characters.")
    else:
        print("✅ No suggestions. Your password is already very strong!")