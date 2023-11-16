import re
enter = str(input())


def calculator(a):
    r = "/|%|-"
    b = re.split(r, a)
    c = a.split("*")
    d = a.split("+")
    if len(b) == 1 and len(c) == 1 and len(d) == 1:
        print("Incorrect expression!")
    elif len(b) > 1:
        x = int(b[0])
        y = int(b[1])
        if "/" in a:
            print(x / y)
        elif "%" in a:
            print(x % y)
        else:
            print(x - y)
    elif len(c) > 1:
        x = int(c[0])
        y = int(c[1])
        print(x * y)
    else:
        x = int(d[0])
        y = int(d[1])
        print(x + y)


calculator(enter)

print("hello world!")
print("hello world!")
print("hello world!")

