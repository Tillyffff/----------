#Задание1
# def p(n):
#   if n > 1:
#     p(n - 1)  
#   print(n)  
# n = int(input())
# print(p(n))

#Задание2
# def print_ab(a, b):
#   print(a)
#   if a == b:
#     return
#   if a < b:
#     print_ab(a + 1, b)
#   else:
#     print_ab(a - 1, b)
# a = int(input())
# b = int(input())
# print_ab(a, b)

#Задание3
# def p(a):
#   if a == 0:
#     return 0
#   return (a % 10) + p(a // 10)
# a = int(input())
# print(p(a))

#Задание4
def g(n, d=2):
  if d * d > n:
    if n > 1:
      print(n)
    return
  if n % d == 0:
    print(d)
    g(n // d, d)
  else:
    next_d = d + 1 if d == 2 else d + 2
    g(n, next_d)

n = int(input())
g(n)