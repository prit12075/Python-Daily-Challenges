import random
import pandas as pd
import numpy as np
import math
import copy

def generate_students(n):
    data = []
    for i in range(1, n + 1):
        student = {
            "id": i,
            "marks": random.randint(40, 95),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data):
    for i in range(len(data)):
        if i % 2 == 0:   # Personalized rule for reg no ending 8
            data[i]["marks"] += int(math.sqrt(data[i]["marks"]))
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 3

def analyze(data):
    marks = np.array([x["marks"] for x in data])

    mean = np.mean(marks)
    median = np.median(marks)
    std = np.std(marks)

    manual_mean = sum(marks) / len(marks)

    normalized = (marks - mean) / std

    return mean, median, std, manual_mean, normalized

def classify(drift, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < 2:
        return "Stable Data"
    elif drift < 5:
        return "Minor Drift"
    else:
        return "Critical Drift"

students = generate_students(10)

shallow = copy.copy(students)
deep = copy.deepcopy(students)

mutate_data(shallow)
mutate_data(deep)

df_original = pd.DataFrame(students)
df_shallow = pd.DataFrame(shallow)
df_deep = pd.DataFrame(deep)

orig_mean = analyze(students)[0]
deep_mean = analyze(deep)[0]
std_dev = analyze(deep)[2]

drift = abs(orig_mean - deep_mean)

result = classify(drift, students, shallow)

print("ORIGINAL DATA")
print(df_original)

print("\nSHALLOW COPY")
print(df_shallow)

print("\nDEEP COPY")
print(df_deep)

print("\nDrift Value =", drift)
print("Tuple =", (deep_mean, drift, std_dev))
print("Final Classification =", result)

print("\nExplanation:")
print("Shallow copy shares nested objects, so modifying scores also changes original data.")