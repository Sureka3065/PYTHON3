def countstrings(n, start):
    if n == 0:
       return 1
    cnt = 0
    for i in range(start, 5):
        cnt += countstrings(n - 1, i)
    return cnt
def countVowelStrings(n):
    return countstrings(n, 0)
n = 4
print(countVowelStrings(n))

