string = input()
match = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
reverse = [ match[i] for i in string[::-1]]
print("".join(reverse))
