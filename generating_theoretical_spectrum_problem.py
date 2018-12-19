string = input()
map = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

array = []
n = len(string)
for i in range(n): array.append(map[string[i]])
for i in range(n): array.append(array[i])

result = [0]
for i in range(n):
    count = 0
    for j in range(n-1):
        count += array[i+j]
        result.append(count)

count = 0
for i in range(n):
    count += array[i]
result.append(count)

result.sort()
for i in range(len(result)):
    result[i] = str(result[i])

print(" ".join(result))
