# # Задание 1
# import random
# n = 20
# b = [random.randint(2, 103) for _ in range(n)]
# print("Исходный массив:")
# print(b)
# for i in range(len(b) - 1):
#     min_idx = i
#     for j in range(i + 1, len(b)):
#         if b[j] < b[min_idx]:
#             min_idx = j
#     if min_idx != i:
#         b[i], b[min_idx] = b[min_idx], b[i]
# print("Отсортированный массив:")
# print(b)

# Задание 2
# import random
# n = 20
# b = [random.randint(0, 100) for _ in range(n)]
# print("Исходный массив:")
# print(b)
# for i in range(len(b) - 1):
#     max_idx = i
#     for j in range(i + 1, len(b)):
#         if b[j] > b[max_idx]:
#             max_idx = j
#     if max_idx != i:
#         b[i], b[max_idx] = b[max_idx], b[i]
# print("отсортированный массив:")
# print(b)


def pphones(phones: list[str]) -> list[str]:
    n = len(phones)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if phones[j] < phones[min_idx]:
                min_idx = j
        if min_idx != i:
            phones[i], phones[min_idx] = phones[min_idx], phones[i]
    return phones
phone_numbers = [
    "54-12-89",
    "23-45-67",
    "11-02-45",
    "99-88-77",
    "23-11-00",
    "45-67-89",
]
print("Исходный список:")
for phone in phone_numbers:
    print(phone)
pphones(phone_numbers)
print("Отсортированный список:")
for phone in phone_numbers:
    print(phone)