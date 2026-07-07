from analyzer import check_password
from generator import generate_password

while True:
  print("\n===== PASSWORD STRENGTH ANALYZER =====")
  print("1. Analyze Password")
  print("2. Generate Strong Password")
  print("3. Exit")

  choice = input("Enter your choice: ")

  if choice == "1": 
     password = input("Enter your password: ")
     check_password(password)

  elif choice == "2":
    new_password = generate_password()
    print(f"\nGenerated Password: {new_password}")

  elif choice == "3":
    print("Thank you for using the Password Strength Analyzer!")
    break
    
  else:
   print("Invalid choice. Please try again.")