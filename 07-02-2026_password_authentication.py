import hashlib
import re
import getpass

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_strength(password: str) -> str:
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    return ["Weak","Medium","Strong","Very Strong"][max(0, min(3, score-2))]

def register():
    pwd = getpass.getpass("Create password: ")
    print("Strength:", check_strength(pwd))
    return hash_password(pwd)

def login(stored_hash):
    pwd = getpass.getpass("Enter password: ")
    print("Access Granted ✅" if hash_password(pwd)==stored_hash else "Access Denied ❌")

if __name__ == "__main__":
    h = register()
    login(h)
