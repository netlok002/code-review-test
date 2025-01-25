import os
import subprocess
import random
from faker import Faker

# Initialize Faker for generating random commit messages
fake = Faker()

# Define some fake developer emails
developers = [
    {"name": "Sam Dev", "email": "sam@example.com"},
    {"name": "Antoinette Dev", "email": "antoinette@example.com"},
    {"name": "Jeff Dev", "email": "jeff@example.com"},
]

# Path to your local Git repository
repo_path = os.path.dirname(os.path.abspath(__file__))

def make_commit():
    """Simulates a commit from a randomly chosen fake developer."""
    dev = random.choice(developers)
    os.chdir(repo_path)

    # Change git user identity for the commit
    subprocess.run(["git", "config", "user.name", dev["name"]])
    subprocess.run(["git", "config", "user.email", dev["email"]])

    # Create a dummy file with random content
    filename = f"test_{random.randint(1, 100)}.txt"
    with open(filename, "w") as f:
        f.write(fake.sentence())

    # Stage, commit, and push changes
    subprocess.run(["git", "add", filename])
    commit_message = fake.sentence()
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "origin", "main"])

    print(f"Committed as {dev['name']} - {commit_message}")

if __name__ == "__main__":
    num_commits = int(input("Enter the number of commits to generate: "))
    for _ in range(num_commits):
        make_commit()
    print("Fake commits successfully pushed!")
