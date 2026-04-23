import random
import math
import numpy as np
import pandas as pd

# ── Data Generation ──────────────────────────────────────────────────────────
def generate_data(n):
    random.seed(11578)
    records = []
    for i in range(1, n + 1):
        sid = f"STU{i:03d}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        records.append((sid, marks, attendance, assignment))
    return records


# ── Classification ────────────────────────────────────────────────────────────
def classify_students(df):
    categories = {"At Risk": [], "Average": [], "Good": [], "Top Performer": []}
    for _, row in df.iterrows():
        sid = row["student_id"]
        m = row["marks"]
        a = row["attendance"]
        if m < 40 or a < 50:
            categories["At Risk"].append(sid)
        elif m > 90 and a > 80:
            categories["Top Performer"].append(sid)
        elif 71 <= m <= 90:
            categories["Good"].append(sid)
        else:
            categories["Average"].append(sid)
    return categories


# ── Advanced Analysis ─────────────────────────────────────────────────────────
def analyze_data(df):
    marks_arr = np.array(df["marks"], dtype=float)
    attend_arr = np.array(df["attendance"], dtype=float)

    mean_marks = np.mean(marks_arr)

    # Manual median (no .describe())
    sorted_m = sorted(marks_arr)
    n = len(sorted_m)
    median_marks = (sorted_m[n // 2 - 1] + sorted_m[n // 2]) / 2 if n % 2 == 0 else sorted_m[n // 2]

    std_marks = np.std(marks_arr)
    max_marks = np.max(marks_arr)

    correlation = np.corrcoef(marks_arr, attend_arr)[0][1]

    min_m, max_m = np.min(marks_arr), np.max(marks_arr)

    # performance_index: weighted score amplified by log of attendance
    # log(attendance+1) rewards consistent attendance while dampening low-attendance scores
    df = df.copy()
    df["normalized_marks"] = [(x - min_m) / (max_m - min_m) for x in marks_arr]
    df["performance_index"] = [
        (m * 0.6 + a * 0.4) * math.log(att + 1)
        for m, a, att in zip(df["marks"], df["assignment"], df["attendance"])
    ]

    stats_tuple = (round(mean_marks, 2), round(std_marks, 2), int(max_marks))
    return df, stats_tuple, round(correlation, 4), round(median_marks, 2)


# ── Pattern Detection ─────────────────────────────────────────────────────────
def detect_patterns(df, categories, std_dev):
    low_att_count = sum(1 for att in df["attendance"] if att < 50)
    top_count = len(categories["Top Performer"])

    print("\n=== Pattern Detection ===")
    print(f"  Consistency     : {'YES – std dev < 15' if std_dev < 15 else 'NO – high variance'}")
    print(f"  Attendance Risk : {'YES – ' + str(low_att_count) + ' students below 50%' if low_att_count > 3 else 'NO – only ' + str(low_att_count) + ' below 50%'}")
    print(f"  High Achievement: {'YES – ' + str(top_count) + ' top performers' if top_count >= 2 else 'NO – only ' + str(top_count) + ' top performer(s)'}")

    if std_dev < 15 and top_count >= 2:
        insight = "Stable Academic System"
    elif low_att_count > 3:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"

    print(f"\n  Final System Insight: {insight}")
    return insight


# ── Main ──────────────────────────────────────────────────────────────────────

# Last digit of AP24110011578 = 8 → personalized count
# Base minimum = 10, personalized addition = 8  →  total = 18 students
NUM_STUDENTS = 18

records = generate_data(NUM_STUDENTS)
student_ids_set = {r[0] for r in records}  # Set of IDs

df = pd.DataFrame(records, columns=["student_id", "marks", "attendance", "assignment"])

print("=" * 65)
print("   MULTI-DIMENSIONAL ACADEMIC INTELLIGENCE SYSTEM")
print("=" * 65)

print("\n=== Student DataFrame ===")
print(df.to_string(index=False))

categories = classify_students(df)
print("\n=== Categorized Dictionary ===")
for cat, students in categories.items():
    print(f"  {cat:15s}: {students}")

df, stats_tuple, correlation, median_marks = analyze_data(df)
mean_marks, std_marks, max_marks = stats_tuple

print("\n=== Statistical Summary ===")
print(f"  Mean Marks        : {mean_marks}")
print(f"  Median Marks      : {median_marks}")
print(f"  Std Deviation     : {std_marks}")
print(f"  Max Marks         : {max_marks}")
print(f"  Correlation (marks vs attendance): {correlation}")
print(f"\n  Stats Tuple → (mean={mean_marks}, std_dev={std_marks}, max_marks={max_marks})")

print("\n=== Normalized Marks & Performance Index ===")
display_cols = ["student_id", "marks", "attendance", "assignment", "normalized_marks", "performance_index"]
print(df[display_cols].round(4).to_string(index=False))

# List comprehension: top performers by performance index
top_pi = [row["student_id"] for _, row in df.iterrows() if row["performance_index"] > df["performance_index"].mean()]
print(f"\n  Students above avg Performance Index: {top_pi}")

detect_patterns(df, categories, std_marks)
