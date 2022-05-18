import itertools
import string
count = 0
wordlist =[]
string = input()

resultado = itertools.permutations(string, len(string))

for caracter in resultado:
    wordlist.append(''.join(caracter))
    count+= 1
print(count)   