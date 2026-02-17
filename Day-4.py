register_number = "AP24110011578"
D = int(register_number[-1])

print("Register Digit (D):", D)

n = int(input("Enter number of activity scores: "))

activity_scores = [0] * n

for i in range(n):
    score = int(input("Enter activity score: "))
    activity_scores[i] = score

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid_count = 0
ignored_count = 0
removed_count = 0

for score in activity_scores:

    if score < 0:
        ignored_count = ignored_count + 1

    else:
        valid_count = valid_count + 1

        if score <= 30:
            low_risk = low_risk + [score]

        elif score <= 60:
            medium_risk = medium_risk + [score]

        elif score <= 100:
            high_risk = high_risk + [score]

        else:
            critical_risk = critical_risk + [score]

print("\nBefore Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

if D % 2 == 0:
    removed_count = len(low_risk)
    low_risk = []
else:
    removed_count = len(critical_risk)
    critical_risk = []

print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nFinal Summary:")
print("Total Valid Entries:", valid_count)
print("Ignored Entries:", ignored_count)
print("Removed Due to Personalization:", removed_count)