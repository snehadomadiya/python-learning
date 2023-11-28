mylist = [10,22,50,87,71,45,10,78,90,20,50,11,19]

result = 0
count = 0

for el in mylist:
    result = result + el
    count = count + 1

myaverage = result /count

variance = 0
for e in mylist:
  variance = ((myaverage - e) ** 2) + variance

print(variance)

std = variance ** (0.5)
