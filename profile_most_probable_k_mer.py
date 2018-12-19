import sys
message = sys.stdin.readlines()

# message = [
# "CCCCTATAGTTCTTGGTGCAGCGTGCACCCTCGTCTGGTTCGGATACGGGCCTGCCAGGA",
# "5",
# "0.583 0.25 0.417 0.25 0.167",
# "0.083 0.25 0.417 0.333 0.25",
# "0 0.25 0.167 0 0.333",
# "0.333 0.25 0 0.417 0.25"
# ]

for i in range(len(message)):
    message[i] = message[i].replace("\n", "")

string = message[0]
k = int(message[1])

prob_arr = {
    'A' : [float(m) for m in message[2].split(" ")],
    'C' : [float(m) for m in message[3].split(" ")],
    'G' : [float(m) for m in message[4].split(" ")],
    'T' : [float(m) for m in message[5].split(" ")],
}

best_prob = -1
most_prob = ""

for i in range(len(string)-k+1):
    prob = 1.0
    for j in range(k):
        prob = prob * prob_arr[string[i+j]][j]
    if prob > best_prob:
        best_prob = prob
        most_prob = string[i:i+k]

print(most_prob)
