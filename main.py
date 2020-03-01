a = "A"
b = "B"
c = "C"
# print(a, b, c)


def one(arg1):
    res1 = arg1 + "1"
    return res1


def two(arg2):
    res2 = arg2 + "2"
    return res2


def three(arg3):
    res3 = arg3 + "3"
    return res3

get1 = one(a)
get2 = two(b)
get3 = three(c)
lst = [get1, get2, get3]

for i in lst:
    print(i)