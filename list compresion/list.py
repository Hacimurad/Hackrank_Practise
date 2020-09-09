x = int(input())
y = int(input())
z = int(input())
n = int(input())
list = []

for i in range(x):
    for t in range(y):
        for k in range(z):
            if (i + t + k) != n:
                array = [i, t, k]
                list.append(array)

print(list)