import sys
import itertools
message = sys.stdin.readlines()

# message= ["4 1\n",
# "CACTGATCGACTTATC\n",
# "CTCCGACTTACCCCAC\n",
# "GTCTATCCCTGATGGC\n",
# "CAGGGTTGTCTTGTCT"]

for i in range(len(message)):
    message[i] = message[i].replace("\n", "")

# print(message)

k, d = message[0].split(" ")
k = int(k)
d = int(d)

def is_pat(string, patt):
    c = 0
    for i in range(k):
        if string[i] == patt[i]:
            c += 1
    diff = k - c
    if diff > d:
        return False
    else:
        return True

res = []

for patt in itertools.combinations('ATCGATCGATCGATCG', k):
    patt = "".join(patt)

    for i in range(1, len(message)):
        for j in range(0, len(message[i])-k+1):
            if is_pat(message[i][j:j+k], patt):
                break
        else:
            # no matching
            break
    else:
        if patt not in res:
            res.append(patt)




print(" ".join(res))
# print (itertools.combinations('ATCG', d))