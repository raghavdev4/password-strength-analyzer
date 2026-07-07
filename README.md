# 🛡️ Password Strength Analyzer

A Python-based Password Strength Analyzer that evaluates password security based on length, complexity, and uniqueness. The project also generates strong passwords, hashes passwords using SHA-256, and prevents password reuse using an SQLite database.

---

## 📌 Features

- ✅ Analyze password strength
- ✅ Check password length
- ✅ Detect uppercase letters
- ✅ Detect lowercase letters
- ✅ Detect numbers
- ✅ Detect special characters
- ✅ Password strength scoring (0–100)
- ✅ Password improvement suggestions
- ✅ Strong password generator
- ✅ SHA-256 password hashing
- ✅ SQLite database integration
- ✅ Prevent password reuse

---

## 🛠️ Technologies Used

- Python 3
- SQLite3
- hashlib
- random
- string

---## 📂 Project Structure

```
Password-Strength-Analyzer/
│
├── main.py          # Main menu and program flow
├── analyzer.py      # Password strength analysis
├── generator.py     # Strong password generator
├── hasher.py        # SHA-256 password hashing
├── database.py      # SQLite database functions
├── passwords.db     # SQLite database (generated automatically)
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anjaliiiiiiii333/password-strength-analyzer.git
```

### 2. Open the project folder

```bash
cd password-strength-analyzer
```

### 3. Run the project

```bash
python main.py
```

---

## 💻 Sample Menu

```
===== PASSWORD STRENGTH ANALYZER =====

1. Analyze Password
2. Generate Strong Password
3. Exit
```

---

## 🔐 Password Analysis

The analyzer checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Password score
- Password strength
- Suggestions for improvement

---

## 🔑 Password Generator

Generates a random strong password containing:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
---

## 🔒 SHA-256 Hashing

Passwords are converted into SHA-256 hashes before storage.

This ensures passwords are **never stored in plain text**.

---

## 🗄️ SQLite Database

The application stores password hashes in an SQLite database.

If a previously used password is entered again, the program detects it and prevents reuse.

---

## 🎯 Learning Outcomes

This project helped me learn:

- Python programming
- Functions and modules
- Password security principles
- SHA-256 hashing
- SQLite database operations
- Git & GitHub workflow
- Basic cybersecurity concepts

---

## 🚀 Future Improvements

- Password entropy calculation
- Dictionary attack detection
- Common password blacklist
- Password breach API integration
- GUI version using Tkinter
- Password history management

---

## 👩‍💻 Author

**Raghavdev**

BCA Cyber Security Student

GitHub: https://github.com/raghavdev4