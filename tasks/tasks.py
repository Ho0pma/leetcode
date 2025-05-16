# 1)
# задача: схлопнуть словарь с любым количеством вложенностей в набор кортежей по примеру:
# a = {
#   b: 4,
#   c: {d: 3, e: 5},
# }
#
# res: [(‘b’, 4), (‘c.d’, 3), (‘c.e’, 5)]

# Solution:
# a = {
#   'b': 4,
#   'c': {'d': 3, 'e': 5},
# }
# result = []
#
# def dict_to_lst(d, prefix=None):
#     for i in d.items():
#         if isinstance(i[1], dict):
#             dict_to_lst(i[1], i[0])
#         else:
#             current = (f'{prefix}.{i[0]}', i[1]) if prefix else i
#             result.append(current)
#
#     return result
#
#
# print(dict_to_lst(a))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 2)
# задача: Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратным пяти - слово Buzz, если число кратно пятнадцати,
# то программа должна выводить слово FizzBuzz.

# Solution:
# result = ''
# for i in range(1, 16):
#     if i % 15 == 0:
#         result += "FizzBuzz"
#     elif i % 3 == 0:
#         result += 'Fizz'
#     elif i % 5 == 0:
#         result += 'Buzz'
#     else:
#         result += str(i)
#
# print(result)

# второй вар
# for i in range(1, 16):
#     result = ""
#     if i % 3 == 0:
#         result += "Fizz"
#     if i % 5 == 0:
#         result += "Buzz"
#     print(result or i)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 3)
# a = 1
# a1 = a
# a1 += 2
# print(a) #?

# 5)
# b = '1'
# b1 = b
# b1 += '2'
# print(b) #?

# 6)
# c = [1]
# c1 = c
# c1.append(2)
# print(c) #?

# 7)
# def funcX():
#     return 42
#
#
# a = funcX
# b = 'funcX'
#
# print(a)  #?
# print(b)  #?

# 8)
# d = {0: 1, 1: 2}
# try:
#     x = d.get('0', 0)
# except:
#     x = 3
#
# print(x)  # ?
# print(x or 5)  # ?

# 9)
# a = '123456789a'
# b = '123456789a'
# print(a == b) # ?
# print(a is b) # ?

# 10)
# a = '123456789'
# a += 'a'
# b = '123456789a'
# print(a == b) # ?
# print(a is b) # ?

# 11)
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) #?
# print(a is b) #?

# 12)
# a = frozenset({1, 2, 3})
# b = frozenset({1, 2, 3})
# print(a == b) #?
# print(a is b) #?

# 13)
# a = {1, 2, 3}
# b = {1, 2, 3}
# print(a == b) #?
# print(a is b) #?


# 14) декоратор с пробросом аргументов

def outer(a=1):
    def decorator_some_func(func):
        def wrapper(*args, **kwargs):
            print(a)  # 1234
            print('before')
            result = func(*args, **kwargs)
            print('after')
            return result

        return wrapper

    return decorator_some_func


@outer(a=1234)
def some_func():
    print('func')


# some_func()
dec = outer(1234)
some_func_dec = dec(some_func)
some_func_dec()
