mylist = [2,3,1,3,5]
has_duplicates = False

mylist.sort()

for num in range(len(mylist)-1):
    if mylist[num] == mylist[num+1]:
        has_duplicates = True
        break
print(has_duplicates)
