palindrome1 = 0
nopalindrome = 0
odd = 0
even = 0
noparity = 0

def parity(num):
    global noparity
    global odd
    global even
    if "." in num:
        noparity += 1
        return "cannot have parity"
    if int(num) % 2 != 0:
        odd += 1
        return 'has odd Parity'
    else:
        even = +1
        return 'has even Parity'


def palindrome(word):
    global nopalindrome
    global palindrome1
    if word is None:
        nopalindrome += 1
        return "Not palindrome"
    N = len(word)
    for i in range(0, int(N / 2)):
        if word[i] != word[N - 1 - i]:
            nopalindrome += 1
            return "Not a Palindrome"
        i += 1
    palindrome1 += 1
    return "a Palindrome"


fdata = open('', 'r')
fdata1 = fdata.readlines()
file = open('', 'w')
file1 = open('', 'w')
for i in fdata1:
    word = i.split('\n')
    word1 = word[0].split(' ')
    num = (word1[0])
    w = word1[1]
    file.write("{} {} and {} is {}.\n".format(num, parity(num), w, palindrome(w)))
total = even + odd + noparity
total1 = nopalindrome + palindrome1
records = {"Percentage of odd parity": (odd / total * 100),
           "Percentage of even parity": (even / total * 100),
           "Percentage of no parity": (noparity / total * 100),
           "Percentage of palindrome": (palindrome1 / total1 * 100),
           "Percentage of non-palindrome": (nopalindrome / total1 * 100)}
for key, value in records.items():
    file1.write(f'{key}: {int(value)}%' + '\n')
