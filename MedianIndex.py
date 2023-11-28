mylist = [10,50,44,85,7,5,55,10,7,20,41,2,3,9]

mylist.sort()
length = len(mylist)
if length % 2 == 1:
  median_index =(length // 2) - 1
  print(mylist[median_index])

else:
  median_index =(length // 2) - 1
  print((mylist[median_index] + mylist[median_index + 1]) / 2)