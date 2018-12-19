m = input()
spectr = m.split(' ')

for i in range(len(spectr)):
    spectr[i] = int(spectr[i])

arr2 = [ 57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

arr = []

for i in arr2:
    if i in spectr:
        arr.append(i)

n = len(arr)

def compare_spectr(res):
    result = [0]
    copy = res.copy()
    for i in range(len(res)):
        copy.append(res[i])

    for i in range(len(res)):
        count = 0
        for j in range(len(res) - 1):
            count += copy[i + j]
            result.append(count)

    count = 0
    for i in range(len(res)):
        count += copy[i]
    result.append(count)
    result.sort()

    if result != spectr:
        return False
    else:
        return True

final_res = []

def true_check(res):
    count = 0
    for i in res:
        if count not in spectr or count > spectr[len(spectr)-1]:
            return False
        count += i
    if count == spectr[len(spectr)-1]:
        if compare_spectr(res):
            final_res.append(res)
        return False
    return True

def search(res, sum):
    if sum not in spectr or sum > spectr[len(spectr)-1]:
        return
    elif sum == spectr[len(spectr)-1]:
        return true_check(res)
    else:
        for i in range(n):
            res1 = res.copy()
            res1.append(arr[i])
            search(res1, sum + arr[i])

for i in range(n):
    res = [arr[i]]
    search(res, arr[i])

for res in final_res:
    for i in range(len(res)):
        res[i] = str(res[i])
    print("-".join(res), end=' ')
