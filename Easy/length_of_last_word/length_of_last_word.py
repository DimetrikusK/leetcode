def lengthOfLastWord(s):
    sepa = s.split()
    return len(sepa[-1])


s = "Hello World"
print(lengthOfLastWord(s))