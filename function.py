""" def name():
    print("sneha")

def surname():
    print("domadiya")
surname()
name() """

""" def ages(name):
    print(name + " is 25 year.")
ages("sneha")
ages("chirag")
ages("hiyan") """


""" def my_function(fname, lname):
  print(fname + " from " + lname)

my_function("sneha", "india")
my_function("smit", "england")
my_function("venus", "paris")
my_function("yashvi", "Canada") """
 
""" def my_function(fname, lname,year):
  print(fname + " from " + lname + " age of " + str(2024-year))

my_function("sneha", "india", 1998)
my_function("smit", "england", 2001)
my_function("venus", "paris", 2000)
my_function("yashvi", "Canada", 1999) """



list = [
    ["sneha","india",1998],
    ["smit","england",2000],
    ["venus","canada",2001],
    ["yashvi","newzealand",2002]
]

""" def disply(name,country,year):
     print(name + " from " + country + " and age of " + str(2024-year)) 

for i in list:
     if 2024-i[2] > 23: 
      disply(i[0],i[1],i[2]) """

print(list)
print("----------------------")
list.append(["chirag","india",1995])

print(list)




