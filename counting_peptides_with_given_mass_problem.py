m = int(input())
arr = [ 57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
results = [0 for i in range(m+1)]
flags = [False for i in range(m+1)]

def foo(sum):
    if sum < 57 or flags[sum]:
        return results[sum]
    flags[sum] = True
    for i in arr:
        if i == sum: results[sum]+=1
    for i in arr: results[sum] += foo(sum-i)
    return results[sum]
print(foo(m))
