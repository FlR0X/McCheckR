# Minecraft Username Checker

A simple Minecraft username checker that uses the Mojang API to verify username availability. Includes proxy support (available upon reaching 15 stars ⭐).

---

## ⭐ Features
- **Mojang API Integration**: Checks Minecraft usernames directly through the Mojang API.
- **Organized Output**: Results are saved as `.txt` files for claimed, unclaimed, and unknown statuses.
- **Proxy Support**: Add proxy support when the repository reaches 15 stars.

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python installed. You’ll need to install the required packages.

### 2. Installation
1. Clone the repository and navigate to the directory.
2. Install the dependencies:
   pip install -r requirements.txt

### 3. Usage
1. Add usernames to check in `usernames.txt`, one username per line.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   cd path/to/directory
4. Run the checker:
   python check.py

---

## 📂 Output
The results will be saved in the following files, organized by date and time:
- `claimed [date - time].txt`: Usernames that are currently claimed.
- `unclaimed [date - time].txt`: Usernames that are available.
- `unknown [date - time].txt`: Usernames with unknown status.

---

## 💬 Notes
- Ensure `usernames.txt` is populated with the usernames you want to check.
- Proxy support will be added once the repository reaches 15 stars ⭐.

---

Thank you for using this tool, and have a great day!
