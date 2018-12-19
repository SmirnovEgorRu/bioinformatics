map = {'UUU' : 'F',
'CUU' : 'L',
'AUU' : 'I',
'GUU' : 'V',

'UUC' : 'F',
'CUC' : 'L',
'AUC' : 'I',
'GUC' : 'V',

'UUA' : 'L',
'CUA' : 'L',
'AUA' : 'I',
'GUA' : 'V',

'UUG' : 'L',
'CUG' : 'L',
'AUG' : 'M',
'GUG' : 'V',

'UCU' : 'S',
'CCU' : 'P',
'ACU' : 'T',
'GCU' : 'A',

'UCC' : 'S',
'CCC' : 'P',
'ACC' : 'T',
'GCC' : 'A',

'UCA' : 'S',
'CCA' : 'P',
'ACA' : 'T',
'GCA' : 'A',

'UCG' : 'S',
'CCG' : 'P',
'ACG' : 'T',
'GCG' : 'A',

'UAU' : 'Y',
'CAU' : 'H',
'AAU' : 'N',
'GAU' : 'D',

'UAC' : 'Y',
'CAC' : 'H',
'AAC' : 'N',
'GAC' : 'D',

'UAA' : 'STOP',
'CAA' : 'Q',
'AAA' : 'K',
'GAA' : 'E',

'UAG' : 'STOP',
'CAG' : 'Q',
'AAG' : 'K',
'GAG' : 'E',

'UGU' : 'C',
'CGU' : 'R',
'AGU' : 'S',
'GGU' : 'G',

'UGC' : 'C',
'CGC' : 'R',
'AGC' : 'S',
'GGC' : 'G',

'UGA' : 'STOP',
'CGA' : 'R',
'AGA' : 'R',
'GGA' : 'G',

'UGG' : 'W',
'CGG' : 'R',
'AGG' : 'R',
'GGG' : 'G',}

def trasnscrib(str):
    return str.replace("T", "U")

def reverse_comp(str):
    match = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse = [match[i] for i in str[::-1]]
    return "".join(reverse)

string = input()
gen_code = input()

res = []
k = len(gen_code)
for i in range(len(string)-k*3+1):
    t1 = trasnscrib(reverse_comp(string[i: i + 3 * k]))

    for j in range(k):
        cur = t1[j*3: j*3 + 3 ]
        t2 = map[cur]
        if t2 != gen_code[j] : break
    else:
        res.append(string[i: i + 3 * k])
        continue

    for j in range(k):
        cur = string[ i+j*3 : i+j*3 + 3 ]
        t2 = map[trasnscrib(cur)]
        if t2 != gen_code[j]: break
    else:
        res.append(string[i:i+3*k])
        continue


print("\n".join(res))
