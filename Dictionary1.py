# Python Dictionary = JSON
# carBrands = ["Nissan", "Toyota", "Mitsubishi", "Tesla"]
# print(carBrands[1])
#
# carMarket = {"Address": "Bauskas Street 22",
#              "Car_Count": 245,
#              "Total_Tax": 1455.6,
#              "isWorking": True,
#              "CarModelsToSell": ["Ford", "Fiat", "Audi", "Subaru"]
#              }
#
# print(type(carMarket))
#
# print(carMarket["CarModelsToSell"][1])

personDictionary = {
    "Person1": {"Name": "Alex", "Age": 34, "IsLucky": False, "Weight": 86.3},
    "Person2": {"Name": "Marta", "Age": 27, "IsLucky": True, "Weight": 62},
    "Person3": {"Name": "Ilze", "Age": 12, "IsLucky": True, "Weight": 32},
    "Person4": {"Name": "Raimonds", "Age": 45, "IsLucky": False, "Weight": 78.5},
    "Person5": {"Name": "Laura", "Age": 30, "IsLucky": True, "Weight": 59}
}

# 1. Write full information about person 3
print("Person3 info:", personDictionary["Person3"])
# 2. Get age of all persons
print("Ages of all persons:")
for person in personDictionary.values():
    print(person["Age"])
# 3. Get person1 weight
print("Person1 weight:", personDictionary["Person1"]["Weight"])
# 4. Print all person names
print("All person names:")
for person in personDictionary.values():
    print(person["Name"])
# 5. Print only lucky persons
print("Lucky persons:")
for person in personDictionary.values():
    if person["IsLucky"]:
        print(person["Name"])
# Print oldest person
age = personDictionary["Person1"]["Age"]
oldest_person_name = "Person1"
for person in personDictionary.values():  # Only values, no key
    if person["Age"] > age:
        age = person["Age"]
        oldest_person_name = person["Name"]
print("Oldest person:", oldest_person_name, "-", age, "years")

# Print youngest person
age = personDictionary["Person1"]["Age"]
youngestPersonName = "Person1"
for person in personDictionary.values():
    if person["Age"] < age:
        age = person["Age"]
        youngestPersonName = person["Name"]
print("Youngest person is", youngestPersonName, "with the age of", age, "years")
