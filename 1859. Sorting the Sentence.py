s = "is2 sentence4 This1 a3"
dc=dict()
for i in s.split():
    dc[i[len(i)-1]]=i[:-1]
s=list()
new=sorted(dc.keys())
for i in new:
    s.append(dc[i])
print(' '.join(s))