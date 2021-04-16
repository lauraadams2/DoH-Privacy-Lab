

f = open("capture01.txt","r")
f1 = f.readlines()

for x in f1:
	src = (x.split()[2])
        dst = (x.split()[4])

	if(("104.16.248.249" in (x.split()[2])) or ("104.16.249.249" in (x.split()[2])) or ("104.16.248.249" in (x.split()[4])) or ("104.16.249.249" in x.split()[4])):
		print x


f.close()
