nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
new=[]
for i in nums1:
    if i in nums2:
        new.append(i)
print(new)