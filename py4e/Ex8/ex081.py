fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word=line.rstrip().split()
    for x in word:
        if x in lst:
            continue
        else:
            lst.append(x)
lst.sort()
print(lst)
