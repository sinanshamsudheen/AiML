cities=["Mumbai","New York","Paris"]
countries=["India","USA","France"]

z=zip(cities,countries)
print(z)
for a in z:
    print(a)

dicti={city:country for city,country in zip(cities,countries)}
print(dicti)

d = dict(zip(cities, countries))
print(d)

# <zip object at 0x000001EB9E8C4AC0>
# ('Mumbai', 'India')
# ('New York', 'USA')
# ('Paris', 'France')
# {'Mumbai': 'India', 'New York': 'USA', 'Paris': 'France'}
# {'Mumbai': 'India', 'New York': 'USA', 'Paris': 'France'}