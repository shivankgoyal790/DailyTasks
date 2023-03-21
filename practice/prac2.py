# function to print alternate uppaer and lowercase letters

def myfunc(a):
    b = ''
    c = len(a)
    for x in range(0, c):
        if x % 2 == 0:
            b += a[x].upper()
        else:
            b += a[x].lower()
    return b


print(myfunc("shivank"))

# map & filter functions


def checkeven(n):
    if n % 2 == 0:
        return True


mylist = [1, 2, 3, 4, 5, 6]
print(list(map(checkeven, mylist)))
print(list(filter(checkeven, mylist)))


# lambda function


# for checkeven function

lambda num: num % 2 == 0
print(list(filter(lambda num: num % 2 == 0, mylist)))
