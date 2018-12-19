N = int(input())
m = input()

# N = 9
# m = "0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388 398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700 701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073"

spectr = m.split(' ')

for i in range(len(spectr)):
    spectr[i] = int(spectr[i])

arr = [ 57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186 ]

n = len(arr)

def score(res):
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

    dict_res = {}
    for i in result:
        if i in dict_res:
            dict_res[i] = dict_res[i] + 1
        else:
            dict_res[i] = 1

    dict_pract = {}
    for i in spectr:
        if i in dict_pract:
            dict_pract[i] = dict_pract[i] + 1
        else:
            dict_pract[i] = 1

    res = 0
    for i in dict_res:
        if i in dict_pract:
            res += min(dict_res[i], dict_pract[i])

    return res

leaders = []

def updates_leaders(res, score):
    if len(leaders) < N:
        leaders.append([res, score])
        leaders.sort(key=lambda t: t[1])
    elif leaders[0][1] <= score:
        leaders[0] = [res, score]
        leaders.sort(key=lambda t: t[1])

def sum(res):
    s = 0
    for i in res:
      s += i
    return s

best_pep = []
max = -1

def search(res):
    global best_pep
    global max
    new_res = []
    # print(res)
    for i in range(len(res)):
        for pep in arr:
            n = res[i].copy()
            n.append(pep)
            new_res.append(n)

    # print(new_res)

    to_next_stage = []
    scores = []
    for i in new_res:
        # print(i)
        s = sum(i)
        if s > spectr[len(spectr)-1]:
            pass
        else:
            to_next_stage.append(i)
            scores.append(score(i))
            # if s == spectr[len(spectr)-1]:
            if scores[len(scores)-1] > max:
                # print(best_pep)
                best_pep = i
                max = scores[len(scores)-1]
    if len(to_next_stage) == 0:
        return

    idx = [i for i in range(len(scores))]
    idx.sort(key=lambda x: scores[x])

    end = len(scores) - N
    if end < 0:
        search(to_next_stage)
    else:
        next = []
        for i in range(end, len(scores)):
            next.append(to_next_stage[idx[i]])
        search(next)

start = []
for i in arr:
    start.append([i])
search(start)

# print(best_pep)

for i in range(len(best_pep)):
    best_pep[i] = str(best_pep[i])

print("-".join(best_pep))
