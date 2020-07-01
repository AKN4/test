a = 1
b = 1
listem = [a, b]
for i in range(20):
    a, b = b, a + b

    listem.append(b)
print(listem)