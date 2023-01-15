from random import sample
result = []
list = [i for i in range(1, 101)]
c = list.copy()
for i in range(len(list) // 2):
    b = sample(c, 2)
    c.remove(b[0])
    c.remove(b[1])
    result.append(b)
print(result)

