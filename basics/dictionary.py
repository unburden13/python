# dict() -> built in function
# unsorted list

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    "unknown": "Unknown month"
}

for item in months.items():
    key, value = item  # unbox the tuple
    print(key, value)

# shortcut for the above loop:
# for key, value in months.items():
#     print(key, value)

for item in months.values():
    print(item)

for item in months.keys():
    print(item)

print(months["unknown"])
print(months.get("unknown"))
print(months.get("Con", "Not a valid key"))
print(months[1])

print("July" in months.values())
print(11 in months.keys())
# print(months.items())

# months.copy()
# months.pop() -- removes the specified item and returns the value of the removed item
months.popitem()  # removes the last item
months.update({12: 'Dec'})
months.update({"unknown": "notdefined"})  # if key does not exist a new tuple will be created
print(months)


person = dict(name='Gustav', age="55")  # dict() not so commonly used to create dictionaries
