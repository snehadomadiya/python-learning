""" mylist = [11,45,85,20,11,10,2,4,8,6,2,10,44,5]

mylist.sort()
length = len(mylist)
if length % 2 == 1:
  median_index =(length // 2) - 1
  print(mylist[median_index])

else:
  median_index =(length // 2) - 1
  print((mylist[median_index] + mylist[median_index + 1]) / 2) """

mylist = [100,155,11,852,200,254,698,411,111,200,444]

mylist.sort()
length = len(mylist)
if length % 2 == 1:
  median_index =(length // 2) - 1
  print(mylist[median_index])

else:
  median_index =(length // 2) - 1
  print((mylist[median_index] + mylist[median_index + 1]) / 2)