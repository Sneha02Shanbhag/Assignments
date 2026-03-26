students = {
    "Sneha": {"marks":92},
    "Rahul": {"marks":85},
    "Anita": {"marks":78},
    "Kiran": {"marks":88},
    "Megha": {"marks":95}
}

def grade(m):
    if m>=90: return "A"
    if m>=75: return "B"
    return "C"

topper = max(students, key=lambda s: students[s]["marks"])
avg = sum(s["marks"] for s in students.values())/len(students)

print("Topper:", topper)
print("Average:", round(avg,2))
print("\nReport:")
for name,info in students.items():
    g = grade(info["marks"])
    print(f"{name:10} {info['marks']:3} -> {g}")
