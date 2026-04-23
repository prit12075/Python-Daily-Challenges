import random
import math
import numpy as np
import pandas as pd


roll_last_digit = 8
num_students = max(10, roll_last_digit)  # at least 10 students


def generate_data(n):
    records = []
    for i in range(1, n + 1):
        student_id = f"STU{i:03d}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        records.append((student_id, marks, attendance, assignment))
    return records


def classify_students(df):
    categories = {}
    for _, row in df.iterrows():
        sid = row['student_id']
        marks = row['marks']
        attendance = row['attendance_percentage']

        if marks < 40 or attendance < 50:
            categories[sid] = "At Risk"
        elif marks > 90 and attendance > 80:
            categories[sid] = "Top Performer"
        elif 71 <= marks <= 90:
            categories[sid] = "Good"
        else:
            categories[sid] = "Average"
    return categories


def analyze_data(df):
    marks_arr = df['marks'].to_numpy()
    attendance_arr = df['attendance_percentage'].to_numpy()

    mean_marks = np.mean(marks_arr)
    median_marks = np.median(marks_arr)
    std_marks = np.std(marks_arr)

    manual_max = marks_arr[0]
    for value in marks_arr:
        if value > manual_max:
            manual_max = value

    correlation = np.corrcoef(marks_arr, attendance_arr)[0][1]

    min_marks = np.min(marks_arr)
    max_marks = np.max(marks_arr)

    if max_marks == min_marks:
        normalized = [1 for _ in marks_arr]
    else:
        normalized = [(x - min_marks) / (max_marks - min_marks) for x in marks_arr]

    df['normalized_marks'] = normalized

    summary_tuple = (round(mean_marks, 2), round(std_marks, 2), int(manual_max))

    return {
        'mean': mean_marks,
        'median': median_marks,
        'std': std_marks,
        'correlation': correlation,
        'summary_tuple': summary_tuple
    }


def system_insight(df, categories, stats):
    consistent = stats['std'] < 15
    attendance_risk = (df['attendance_percentage'] < 50).sum() > 3
    high_achievement = list(categories.values()).count("Top Performer") >= 2

    if consistent and high_achievement and not attendance_risk:
        return "Stable Academic System"
    elif attendance_risk:
        return "Critical Attention Required"
    else:
        return "Moderate Performance"


student_records = generate_data(num_students)

columns = ['student_id', 'marks', 'attendance_percentage', 'assignment_score']
df = pd.DataFrame(student_records, columns=columns)

unique_attendance_values = set(df['attendance_percentage'])

df['performance_index'] = [
    round((m * 0.6 + a * 0.4) * math.log(att + 1), 2)
    for m, a, att in zip(
        df['marks'], df['assignment_score'], df['attendance_percentage']
    )
]

categories = classify_students(df)
stats = analyze_data(df)
insight = system_insight(df, categories, stats)

print("\n===== STUDENT DATAFRAME =====")
print(df)

print("\n===== CATEGORY DICTIONARY =====")
print(categories)

print("\n===== STATISTICAL SUMMARY =====")
print(f"Mean Marks      : {stats['mean']:.2f}")
print(f"Median Marks    : {stats['median']:.2f}")
print(f"Std Deviation   : {stats['std']:.2f}")
print(f"Correlation     : {stats['correlation']:.2f}")

print("\nTuple (mean, std_dev, max_marks):")
print(stats['summary_tuple'])

print("\nUnique Attendance Values Count:", len(unique_attendance_values))

print("\n===== FINAL SYSTEM INSIGHT =====")
print(insight)