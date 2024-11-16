import random

cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities, key=lambda c:len(c)))

print(sorted(cities, key=lambda c:len(c.split())))

print(sorted(cities, key=lambda c: c[-1]))

print(sorted(cities, key=lambda c: c[::-1]))

print(sorted(cities, key=lambda c: c.lower().count('a')))

cities_mills = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities_mills, key=lambda c:c[1]))

print(sorted(cities_mills, key=lambda c:c[1] , reverse=True))

print(sorted(cities_mills, key=lambda c:c[2]))

print(sorted(cities_mills, key=lambda c:(c[2], c[1])))


rand_num: list[int] = [random.randint(1, 100) for _ in range(50)]
print(sorted(rand_num))

print(sorted(rand_num, key=lambda r: sum(rand_num) / len(rand_num)))