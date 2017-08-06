import pprint

d = {"earth":"земля", "mars":"марс", "venus":"венера"}
print(d, type(d))

print(d["earth"])
d["mercury"] = "меркурий"
print(d)
# del d["earth"]
# print(d)
# if "earth" in d:
#     print("Earth is found!")
#     del d["earth"]
# else:
#     print("Earth is missing!")
# print(d)
#
if "earth" in d:
    print("Earth is found!")
    del d["earth"]
else:
    print("Earth is missing!")
print(d)

if "земля" in d.values():
    print("Earth is found!")
    del d["earth"]
else:
    print("Earth is missing!")
print(d)

d['venus'] = "Венера"
print(d)


capitals = {"UA":"Kyiv", "GB":"London", "NO":"Oslo", "DE":"Berlin"}
print(capitals)
print(capitals["NO"])

products = {'Apple': ['iPod', 'iPad', 'iPhone', 'iBook'], 'Google': ['Pixel', 'Nexus', 'GoogleGlass']}
print(products)
products['Apple'].append('iWatch')
print(products)

for key in d:
    print(key, '->', d[key])
for key in d.keys():
    print(key, '->', d[key])
for value in d.values():
    print(value)

student1 = {'name':"Alice", 'age':24, "year":2, "grant":1000}
student2 = {'name':"Bob", 'age':22, "year":1}
student3 = {'name':"Bill", 'age':19, "year":1}

group = [student1, student2, student3]
print(group)

for student in group:
    student['year'] +=1

print(group)
pprint.pprint(group)

for student in group:
    if 'grant' in student:
        student["grant"] += 500
    else:
        student['grant'] = 1000

pprint.pprint(group)

