import sys
import itertools
message = sys.stdin.readlines()

# message= ["5\n",
# "GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA",
# "TATATCCACATGACCTCGACAACGCACGGTCGAAT",
# "TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC",
# "TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT",
# "TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT",
# "AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT",
# "CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC",
# "ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT",
# "GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA",
# "ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG",
# ]


for i in range(len(message)):
    message[i] = message[i].replace("\n", "")

k = int(message[0])

def dist(string, patt):
    c = 0
    for i in range(k):
        if string[i] != patt[i]:
            c += 1
    return c

best_res = ""
best_score = 1000000000

for patt in itertools.combinations('ATCG'*k, k):
    patt = "".join(patt)
    dis = 0
    for i in range(1, len(message)):
        local_min_dist = 1000000000
        for j in range(0, len(message[i])-k+1):
            d = dist(message[i][j:j+k], patt)
            if d < local_min_dist:
                local_min_dist = d
        dis += local_min_dist
    if best_score > dis:
        # print(patt)
        best_res = patt
        best_score = dis

print(best_res)