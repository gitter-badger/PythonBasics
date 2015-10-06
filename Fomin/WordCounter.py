s = input('Enter a random string ')
s = s.split()
print({s[i] : s.count(s[i]) for i in range(len(s))})