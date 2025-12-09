# 1
flattened_matrix = [x for row in [[1, 2], [3, 4], [5, 6]] for x in row]
# 2
word_initials = [w[0] for w in ["dog", "cat", "mouse"]]
# 3
positive_numbers = [n for n in [-5, 3, -1, 0, 7, -2] if n > 0]
# 4
parity_1_10 = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
# 5
sqrt_list = [math.sqrt(n) for n in [4, 9, 16, 25]]
# 6
divisible_by_5 = [i for i in range(0, 51) if i % 5 == 0]

print(flattened_matrix)
print(word_initials)
print(positive_numbers)
print(parity_1_10)
print(sqrt_list)
print(divisible_by_5)
