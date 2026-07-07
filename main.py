from analyzer import check_password
from generator import generate_password
from hasher import hash_password
from database import create_database, save_password_hash, password_exists
create_database()
while True:
  print("\n===== PASSWORD STRENGTH ANALYZER =====")
  print("1. Analyze Password")
  print("2. Generate Strong Password")
  print("3. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    password = input("Enter your password: ")

    check_password(password)

    hashed_password = hash_password(password)

    print("\nSHA-256 Hash:")
    print(hashed_password)

    if password_exists(hashed_password):
        print("\n❌ This password has already been used before.")
    else:
        save_password_hash(hashed_password)
        print("\n✅ Password hash saved successfully.")

  elif choice == "2":
    new_password = generate_password()
    print(f"\nGenerated Password: {new_password}")

  elif choice == "3":
    print("Thank you for using the Password Strength Analyzer!")
    break
    
  else:
   print("Invalid choice. Please try again.")