Name = input("Enter your fullname:- ")
n = int(input("Enter the number of requests you want to enter:- "))

requestList = []

for i in range(n):
    request = int(input(f"Enter your request {i+1}:- "))
    requestList.append(request)

low_Demand = []
no_Demand = []
invalid_Requests = []
moderate_Demand = []
high_Demand = []
valid = 0

for req in requestList:
    if req < 0:
        invalid_Requests.append(req)
    else:
        valid += 1
        if req == 0:
            no_Demand.append(req)
        elif req <= 20:
            low_Demand.append(req)
        elif req <= 50:
            moderate_Demand.append(req)
        else :
            high_Demand.append(req)


#Personalization 
L = 0

for char in Name:
    if char == ' ':
        continue
    L += 1

PLI = L%3
removedRequest = 0
if PLI == 0:
    removedRequest = len(low_Demand)
    low_Demand.clear()
elif PLI == 1:
    removedRequest = len(high_Demand)
    high_Demand.clear()
else:
    removedRequest = len(low_Demand) + len(high_Demand) + len(no_Demand) + len(invalid_Requests)
    high_Demand.clear()
    low_Demand.clear()
    no_Demand.clear()
    invalid_Requests.clear()


print("\n----- DISPATCH REPORT -----")

print(f"Length of Name (L): {L}")
print(f"PLI Value: {PLI}")

if PLI == 0:
    print("Applied Rule: A (Low Demand Removed)")
elif PLI == 1:
    print("Applied Rule: B (High Demand Removed)")
else:
    print("Applied Rule: C (Only Moderate Demand Kept)")

print(f"\nTotal Valid Requests: {valid}")
print(f"Total Requests Removed Due to PLI: {removedRequest}")

print("\nFinal Categorized Lists After Filtering:")
print(f"Low Demand: {low_Demand}")
print(f"Moderate Demand: {moderate_Demand}")
print(f"High Demand: {high_Demand}")
print(f"No Demand: {no_Demand}")
print(f"Invalid Requests: {invalid_Requests}")