import pprint
import sys
import collections
import functools

print(sys.version_info)
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

student1 = {'name':"Alice", 'age':24, "year":2, "grant":1000, "bonus":1000, "head_of_":True }
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
print(student1)

group.sort(key=lambda student: student['age'])

pprint.pprint(group)

group.sort(key=lambda student: (student['grant'], student['name']), reverse= True)

print("new")
pprint.pprint(group)

# dict comprephention
# d = {i:chr(i) for i in range(10000+1)}
# pprint.pprint(d)

print(student1)
pprint.pprint(student1)

d = collections.OrderedDict()

d['age'] = 42
d['name'] = 'Bill'
d['title'] = 'CIO'
d['dep'] = 'IT'
d['salary'] = 120000

print(d)

####################################################################
# def print_entry(entry):
#     for key in entry:
#         print("%s:\t%s" %(key, entry[key]))
#
# print_entry(d)

print(d['dep'])

#######################################################################
def compare_students(st1, st2):
    if st1['grant'] == st2['grant'] and st1['name'] == st2['name']:
        return 0
    elif st1['grant'] < st2['grant'] and st1['name'] < st2['name']:
        return -1
    else: # st1['grant'] > st2['grant'] and st1['name'] < st2['name']:
        return 1

group.sort(key=functools.cmp_to_key(compare_students))
pprint.pprint(group)

en2es_dict = {'world': 'mundo',
              'language': 'idioma',
              'bye': 'hasta la vista'}
es2en_dict = {v:k for k, v in en2es_dict.items()}
print(es2en_dict)
print(es2en_dict['mundo'])