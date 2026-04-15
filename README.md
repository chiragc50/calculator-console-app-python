# 🧮 CLI Calculator (Python)

A simple command-line calculator built with Python. This project demonstrates core programming concepts like functions, input validation, control flow, and clean code structure.

---

## 🚀 Features

* Perform basic operations:

  * ➕ Addition
  * ✖️ Multiplication
  * ➖ Subtraction
  * ➗ Division
* Handles invalid input safely (no crashes)
* Prevents division by zero
* Clean and modular code using functions
* Uses a dispatcher dictionary (scalable design)

---

## 📂 Project Structure

```
app.py   # Main script
```

---

## 🛠️ How It Works

1. Displays a menu with available operations
2. User selects an operation (`a`, `m`, `s`, `d`)
3. Prompts user to enter two numbers
4. Performs the calculation
5. Displays result
6. Repeats until user exits

---

## ▶️ Usage

Run the script:

```bash
python app.py
```

Example:

```
-------------Calculator-------------
1.[A]dd
2.[M]ulitply
3.[S]ubstract
4.[D]ivide
5.Press Any Key to Exit

Enter: a

--------------------Addition--------------------
Enter number one: 10
Enter number two: 5
15
```

---

## ⚠️ Error Handling

* Invalid input (non-numeric values):

  ```
  ❌ Please enter valid numbers
  ```

* Division by zero:

  ```
  ❌ Can't divide by zero
  ```

---

## 🧠 Concepts Used

* Functions and modular design
* Exception handling (`try/except`)
* Loops (`while True`)
* Conditional logic
* Dictionary-based dispatch

---


## 📌 Notes

* Input is case-insensitive (`A` or `a` both work)
* Program exits when user enters any key not listed in menu

---


## 📄 License / Copyright

© 2026 Chirag SD

This project is for educational purposes.

You are free to use, modify, and distribute this code for learning purposes.
However, the author is not responsible for any misuse or damages caused by this software.


---

## 🙌 Author

* Chirag SD
* GitHub: https://github.com/chiragc50

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
