
````markdown
# ✅ Auto-Contribution Script for GitHub (`daily-log`)

Automate your daily GitHub contributions by auto-generating a log file and pushing it to your `daily-log` repo. Keep your green squares active the **legit** way!

---

## 🚀 What It Does

- Creates a new Markdown file each day with the current date.
- Commits and pushes it to your GitHub repo.
- Runs automatically every day at 10 AM using `cron`.

---

## 🧩 Prerequisites

- Python 3 installed.
- A GitHub repo cloned locally (e.g., `daily-log`).
- SSH configured for GitHub (no password prompt).
- Git installed and configured.

---

## 🔧 Setup Instructions

### 1. Clone Your Repo

```bash
git clone git@github.com:Root-acess/daily-log.git
cd daily-log
````

> Use SSH URL for seamless automation.

---

### 2. Add the Python Script

Create a file named `auto_contribute.py` and paste the following code:

```python
import os
import datetime
import subprocess

# === CONFIGURATION ===
repo_path = "/home/charon/Desktop/daily-log"  # Replace with your actual path
os.chdir(repo_path)

# === DAILY FILE CREATION ===
today = datetime.date.today().strftime("%Y-%m-%d")
file_name = f"{today}.md"

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write(f"# {today} - Daily Log\n\nToday I made a contribution!")

# === GIT COMMANDS ===
subprocess.call(["git", "pull"])
subprocess.call(["git", "add", file_name])
subprocess.call(["git", "commit", "-m", f"Auto contribution: {today}"])
subprocess.call(["git", "push"])
```

---

## 🧪 Test the Script

```bash
python3 auto_contribute.py
```

* A file like `2025-07-04.md` will be created.
* It will be committed and pushed to your GitHub repo.

---

## ⏰ Automate with Cron (Linux/macOS)

### Step 1: Open your crontab

```bash
crontab -e
```

### Step 2: Add the job (runs every day at 10 AM)

```bash
0 10 * * * /usr/bin/python3 /home/charon/Desktop/daily-log/auto_contribute.py
```

> 🧠 You can check your Python path with `which python3`

---

## 📁 Optional: Log Automation Output

To track if the script ran successfully, update your cron entry like this:

```bash
0 10 * * * /usr/bin/python3 /home/charon/Desktop/daily-log/auto_contribute.py >> /home/charon/Desktop/daily-log/cron_output.log 2>&1
```

---

## 💡 Tips & Enhancements

* Use `.gitignore` to avoid committing `auto_contribute.py` itself:

```bash
echo "auto_contribute.py" >> .gitignore
```

* Add daily motivational quotes or coding tips.
* Switch to GitHub Actions to automate without keeping your PC on.

---

## 🎁 Want More?

✅ Add auto content (quotes, code tips)?
✅ Want to use GitHub Actions instead of cron?

Let me know — I’ll help you supercharge your automation!

---

**Made with ❤️ by Charon**

```

---

Would you like me to save this as a file and give you the download?
```
