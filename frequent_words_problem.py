string = input()
k = int(input())

patterns = {}
for i in range(len(string)-k+1):
    if string[i:i+k] in patterns:
        patterns[string[i:i+k]] = patterns[string[i:i+k]] + 1
    else:
        patterns[string[i:i+k]] = 1

max = 0
max_patterns = []
for elem in patterns:
    if patterns[elem] > max:
        max = patterns[elem]
        max_patterns = [elem]
    elif patterns[elem] == max:
        max_patterns.append(elem)

print(" ".join(max_patterns))
