import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import random
import string


# -----------------------------
# PART 1: Password Scoring Logic
# -----------------------------

def score_password(password):
    score = 0

    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Scoring Rules
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1
    if has_lower:
        score += 1

    return {
        "password": password,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_number": has_number,
        "has_special": has_special,
        "score": score
    }


# -----------------------------
# PART 2: Generate Sample Dataset
# -----------------------------

def generate_random_password():
    length = random.randint(5, 12)
    characters = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(characters) for _ in range(length))


data = []

# Generate 100 sample passwords
for _ in range(100):
    pwd = generate_random_password()
    result = score_password(pwd)
    data.append(result)


# Save to CSV
csv_file = "password_dataset.csv"
keys = data[0].keys()

with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

print("Dataset created and saved to password_dataset.csv")


# -----------------------------
# PART 3: Data Analysis with Pandas
# -----------------------------

df = pd.read_csv(csv_file)

print("\n--- DATA ANALYSIS RESULTS ---")
print("Average Password Score:", round(df["score"].mean(), 2))
print("Most Common Score:", df["score"].mode()[0])
print("Average Password Length:", round(df["length"].mean(), 2))

print("\nPercentage with Special Characters:",
      round(df["has_special"].mean() * 100, 2), "%")

print("Percentage with Uppercase Letters:",
      round(df["has_upper"].mean() * 100, 2), "%")

print("Percentage with Numbers:",
      round(df["has_number"].mean() * 100, 2), "%")


# -----------------------------
# PART 4: Visualisation
# -----------------------------

df["score"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Password Strength Scores")
plt.xlabel("Score (0–5)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
