""" mydictionary = {"name" : "Sneha" , "lastname" : "Domadiya"}

print(mydictionary["lastname"]) """

""" student = [
    {"name": "smit", "age": 28,"course":"Data", "contact":{"number":"56565656","city":"Berlin"}},
    {"name": "sneha", "age": 18,"course":"Data"},
    {"name": "akta", "age": 25,"course":"Health"},
    {"name": "akash", "age": 19,"course":"MBA"},
]

print(student[0]["contact"]) """

student = [
    {"name": "smit", "age": 28,"course":"Data", "contact":{"number":"56565656","city":"Berlin"}},
    {"name": "sneha", "age": 18,"course":"Data"},
    {"name": "akta", "age": 25,"course":"Health", "contact":{"number":"79865525","city":"Munich"}},
    {"name": "akash", "age": 19,"course":"MBA"},
]

print(student[2]["contact"])
print(student[0]["age"])
print(student[2]["name"])
print(student[3]["course"])




