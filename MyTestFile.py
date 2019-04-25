from _ctypes import sizeof
from builtins import print, tuple


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = MyClass("Raman", "23")
print(p1.name + " is my name " + p1.age + " is age")
print('\n')
citylist = list(('newark', 'las vegas', 'yellowstone', 'singapore'))
for x in citylist:
    print(x)

print('\n')
if 'london' in citylist:
    print('city is found')
elif citylist.__len__()==4:
    print(citylist.__len__())
else:
    print('close this if elif else block')

print('\n')
mytuple = tuple(("apple", "banana", "cherry"))
for x in mytuple:
    print(x)

print('\n')
mydictionary = {"freq" : "50", "time" : "daytime", "zone" : "western"}
for x in mydictionary:
     print(mydictionary)
     break
if "freq" in mydictionary:
    print(mydictionary.get("freq"))
    mydictionary['voltage'] = "440kW"
    print(mydictionary.items())
    print('\n')

mydictionary.update('')
