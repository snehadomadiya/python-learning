age = [13, 45, 25, 29, 14, 29, 26, 28]

filter_age = list(filter(lambda x: x > 25, age))

print("Ages greater than 25:", filter_age)

filter_age = list(filter(lambda x: x < 25, age))

print("ages less than 25:", filter_age)

filter_age = list(filter(lambda x: x == 25, age))

print("ages less than 25:", filter_age)