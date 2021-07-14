import sys

total = 0

with open(sys.argv[1], "rt") as myfile:
    for myline in myfile:
        x = myline.split()
        src = x[2]
        dst = x[4]
        a = x[6]
        web = x[7]
        length = x[-1]
        
        if "104.16.248.249" in src or "104.16.249.249" in src or "104.16.248.249" in dst or "104.16.249.249" in dst:
            #print("Source: {0}, Destination: {1}, Length: {2}".format(src,dst,length))
            total += int(length)

print(total)
            
