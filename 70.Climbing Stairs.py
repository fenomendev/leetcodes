n=4
first=0
second=1
for i in range(n):
    result=first+second
    first=second
    second=result
print(result)