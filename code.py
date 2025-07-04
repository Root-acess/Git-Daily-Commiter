import os
import datetime
import subprocess

# Define the path to your repo
repo_path = "/path/to/your/repo"
os.chdir(repo_path)

# Create a file with today's date
today = datetime.date.today().strftime("%Y-%m-%d")
file_name = f"{today}.md"

# Add a simple log or message
with open(file_name, "w") as f:
    f.write(f"# Daily Contribution - {today}\n\nToday I learned something cool.")

# Git commands to add, commit, and push
subprocess.call(["git", "add", file_name])
subprocess.call(["git", "commit", "-m", f"Daily contribution: {today}"])
subprocess.call(["git", "push"])
