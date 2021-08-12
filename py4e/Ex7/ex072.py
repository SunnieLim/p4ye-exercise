fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    num = float(line[line.find(":") + 1 : ])
    total = num + total
avg = total/count
print('Average spam confidence:',avg)
