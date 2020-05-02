# def func(string):
#     if string[0] in ["a", "e", "i", "o", "u"]:
#         return string + "ay"
#     else:
#         string += string[0]
#         string = string[1:]
#         return string + "ay"


# word = func("apple")
# print(word)


# def myfunc(*args):
#     mylist = []
#     print(args)
#     for i in list(args):
#         if i % 2 == 0:
#             mylist.append(i)
#     return mylist


# x = myfunc(5, 6, 7, 8)
# print(x)


# def myfunc(a):
#     b = []
#     for i in range(len(a)):

#         if i % 2 == 0:
#             b.append(a[i].lower())
#         else:
#             b.append(a[i].upper())

#     return "".join(b)


# print(myfunc("abcdeyyyyyyy"))

mylist = [1, 2]

print(mylist.index(3))
