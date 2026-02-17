Name = input("Enter your fullname:- ")
n = int(input("Enter the number of requests you want to enter:- "))

requestList = []

for i in range(n):
    request = int(input(f"Enter your request {i+1}:- "))
    requestList.append(request)
requests = []
low_Demand = []
no_Demand = []
invalid_Requests = []
moderate_Demand = []
high_Demand = []
valid = 0

requests = [no_Demand, low_Demand, moderate_Demand, high_Demand, invalid_Requests]

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
    removedRequest = len(low_Demand) + len(high_Demand)
    high_Demand.clear()
    low_Demand.clear()


print(f"Invalid Re")