


def compute_prob_matrix(motifs):
    k = len(motifs[0])

    count_arr = {
        'A': [0 for m in range(k)],
        'C': [0 for m in range(k)],
        'G': [0 for m in range(k)],
        'T': [0 for m in range(k)],
    }

    for motif in motifs:
        for i in range(len(motif)):
            count_arr[motif[i]][i] += 1

    n = len(motifs)

    for pep in ('A', 'C', 'G', 'T'):
        for i in range(k):
            count_arr[pep][i] = count_arr[pep][i] / n

    return count_arr

def best_motif(string, k, prob_arr):
    best_prob = -1
    most_prob = ""

    for i in range(len(string) - k + 1):
        prob = 1.0
        for j in range(k):
            prob = prob * prob_arr[string[i + j]][j]
        if prob > best_prob:
            best_prob = prob
            most_prob = string[i:i + k]

    return most_prob

def score(motifs, k):
    count_arr = {
        'A': [0 for m in range(k)],
        'C': [0 for m in range(k)],
        'G': [0 for m in range(k)],
        'T': [0 for m in range(k)],
    }

    for motif in motifs:
        for i in range(len(motif)):
            count_arr[motif[i]][i] +=1

    most_req = []
    map = {0:'A', 1:'C', 2:'G', 3:'T'}
    for i in range(len(motifs[0])):
        max_score = 0
        max_idx = 0
        a = [ count_arr['A'][i], count_arr['C'][i], count_arr['G'][i], count_arr['T'][i] ]
        for j in range(len(a)):
            if max_score < a[j]:
                max_score = a[j]
                max_idx = j
        most_req.append(map[max_idx])

    all_score = 0

    for i in range(len(motifs[0])):
        count = 0
        for motif in motifs:
            if motif[i] != most_req[i]:
                count += 1
        all_score += count

    return all_score

import sys
# message = sys.stdin.readlines()

message = [
"5 5",
"TCCCTCCATGTGTAAAGTCCGCCTCTACTTCGAGT",
"GGTAGTACCCCTCTAGAATTATTATCCTTAGGTCA",
"CACGTCGAGGACCGCCGCCGCCATCACAAGCTTTA",
"GCAATGATCCCCGTTTACATCAATAGAGGGGGGAA",
"GACGACCCTAGCTTCTTCTTGAGTTTGTGAAGCGG",
]

for i in range(len(message)):
    message[i] = message[i].replace("\n", "")

k  = int(message[0].split(" ")[0])
t = int(message[0].split(" ")[1])

collect_of_best_motifs = []
best_score = k*t*100

for i in range(len(message[1]) - k + 1):
    cur_coll = [message[1][i:i+k]]
    prob_matrix = compute_prob_matrix(cur_coll)
    for j in range(1,t):
        cur_coll.append(best_motif(message[1+j], k, prob_matrix))
        prob_matrix = compute_prob_matrix(cur_coll)
    s = score(cur_coll, k)
    # print(cur_coll, s)
    if s < best_score:
        collect_of_best_motifs = cur_coll
        best_score = s

for i in collect_of_best_motifs:
    print(i)
