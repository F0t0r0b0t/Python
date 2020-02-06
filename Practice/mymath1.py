import sys


def compare(a, b=10):
    if a >= b:
        print(str(a) + " is bigger")
    else:
        print(str(b) + " is bigger")


x = 1123
print("******")
print(sys.getrefcount(x))
y = 1123
print("******")
print(x is y)
print("******")
print(sys.getrefcount(x))
# x = 10
y = 20
print("******")
print(x is y)
print("******")
print(sys.getrefcount(x))
print("******")
print(sys.getrefcount(y))
print("******")
compare(444, 12)
print("******")
