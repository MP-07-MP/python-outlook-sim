# Outlook Simulator (Python CLI)

A Python-based command-line simulation of an email client (similar to Microsoft Outlook) built using Object-Oriented Programming (OOP) principles. 

This application models email processing, folder movement, status flagging, custom message encryption, and sender text statistics.

---

## Key Features

- **Base Mail Management:** Class representation for handling standard email properties, folder tags, read statuses, and flags.
- **Specialized Email Subclasses:**
  - `Confidential`: Encrypts message bodies using custom position-based encryption logic.
  - `Personal`: Calculates and appends message statistics (word count, average word length, longest word).
- **Mailbox Operations:** Filter emails by sender, search by date, move to folders (e.g., `bin`, `conf`), and mark messages.
- **Interactive CLI:** Command-line interpreter executing user scripts dynamically.

---

## Tech Stack & OOP Concepts Applied

- **Language:** Python 3
- **Concepts:** Inheritance, Polymorphism, Encapsulation (Getters/Setters), Error Handling (`try/except`), String Manipulation.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/MP-07-MP/python-outlook-sim.git](https://github.com/MP-07-MP/python-outlook-sim.git)
