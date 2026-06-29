# 🔑 Password Strength Checker

A Python command-line tool that analyzes the strength of a password based on multiple security criteria, returning a score, a rating, a visual strength bar, and specific improvement suggestions. Built as part of a Cybersecurity Internship task.

---

## 📋 Overview

Weak passwords are one of the leading causes of account compromise. This tool evaluates a password against 5 real security criteria — the same principles used by major password managers and security frameworks — and gives actionable feedback to help users create stronger passwords.

### Sample Output

```
==================================================
        🔑 PASSWORD STRENGTH REPORT
==================================================
  Password : **********
  Length   : 10 characters
  Score    : 5 / 7
  Rating   : 👍 STRONG
  Strength : [██████████████░░░░░░]

  ── What's Good ──
  ✅ Length is acceptable (8+ characters)
  ✅ Contains uppercase letters (A-Z)
  ✅ Contains lowercase letters (a-z)
  ✅ Contains numbers (0-9)

  ── Suggestions ──
  ❌ Add special characters like ! @ # $ % ^ & *
==================================================
```

---

## ✨ How the Scoring Works

Passwords are scored out of **7 points**:

| Criterion | Points | Notes |
|---|---|---|
| Length 8–11 characters | +1 | Minimum acceptable |
| Length 12–15 characters | +2 | Good |
| Length 16+ characters | +3 | Excellent — length matters most |
| Contains uppercase letters [A–Z] | +1 | |
| Contains lowercase letters [a–z] | +1 | |
| Contains digits [0–9] | +1 | |
| Contains special characters [!@#$...] | +1 | |

**Penalties:**

| Condition | Penalty |
|---|---|
| Password is in common password list | Score reset to 0 |
| Same character repeated 3+ times (e.g. `aaa`) | Score − 1 |

**Ratings:**

| Score | Rating |
|---|---|
| 6–7 | 💪 VERY STRONG |
| 4–5 | 👍 STRONG |
| 3 | 😐 MODERATE |
| 1–2 | 😟 WEAK |
| 0 | 🚨 VERY WEAK |

---

## ✅ Features

- 5-criteria scoring system with weighted length scoring
- Visual strength bar using block characters
- Lists exactly what criteria the password passed
- Lists specific suggestions for what to improve
- Common password detection — 10 frequently-used weak passwords blocked
- Repeated character detection using regular expressions
- Empty password handling with a clear error message

---

## 🛠️ Requirements

- Python 3.8+
- No external libraries required — uses only the built-in `re` and `string` modules

```bash
# No installation needed — just run directly
python task3_password_checker.py
```

---

## ▶️ Usage

```bash
python task3_password_checker.py
```

```
Welcome to the Password Strength Checker!

Options: (1) Check a password   (2) Exit
Choice: 1
Enter a password to check: MyPass1!

==================================================
        🔑 PASSWORD STRENGTH REPORT
==================================================
  Password : ********
  ...
```

---

## 🧪 Test Cases (Verified)

| Password | Score | Rating | Notes |
|---|---|---|---|
| `password` | 0 | 🚨 VERY WEAK | Common password — score reset to 0 |
| `abc` | 1 | 😟 WEAK | Too short |
| `hello123` | 3 | 😐 MODERATE | No uppercase or special character |
| `Hello123` | 4 | 👍 STRONG | Missing special character only |
| `Hello123!` | 5 | 👍 STRONG | All 4 types, 9 characters |
| `Tr0ub4dor$3xYz!` | 6 | 💪 VERY STRONG | 16+ chars, all types |
| `aaabbbccc` | 1 | 😟 WEAK | Repeated character penalty applied |
| `ALLUPPERCASE1!` | 5 | 👍 STRONG | No lowercase |
| `12345678` | 2 | 😟 WEAK | Digits only |

All 13 test cases verified and behave as expected.

## 📁 Project Structure

```
.
├── task3_password_checker.py    # Main program
└── README.md                    # This file
```

---

## ⚠️ Note

This tool uses a scoring heuristic based on common password security guidelines (NIST SP 800-63B, OWASP). It is an educational implementation and not a substitute for professional password auditing tools.

---
