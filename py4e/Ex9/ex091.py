fname = input("Enter file name: ")
fh = open(fname)
counts=dict()
for line in fh:
    if  not line.startswith('From '): continue
    sender=line.split()
    emails=sender[1]
    counts[emails]=counts.get(emails,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count> bigcount:
        bigword= word
        bigcount=count
print(bigword,bigcount)
