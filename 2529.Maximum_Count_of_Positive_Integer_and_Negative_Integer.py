nums = [-3,-2,-1,0,0,1,2]
count_musbat=0
count_manfiy=0
for i in nums:
    if i>0:
        count_musbat+=1
    elif i<0:
        count_manfiy+=1
print(max(count_musbat,count_manfiy))