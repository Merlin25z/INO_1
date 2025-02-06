s = []
a = int(input())
s.append(a)
b = int(input())
s.append(b)
c = int(input())
s.append(c)
s.sort()
print(s[2],s[0],s[1],sep="\n")
