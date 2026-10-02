temperatures_c = [-10, 0, 17.6, 28, 100]
c_to_f = lambda c: (c * 9/5) + 32
temperatures_f = list(map(c_to_f, temperatures_c))
print(temperatures_f)