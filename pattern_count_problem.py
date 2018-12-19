pattern = input()
string = input()
count = 0
k = len(pattern)
for i in range(len(string)-k+1):
    if string[i:i+k] == pattern: count +=1
print(count)