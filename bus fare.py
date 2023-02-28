fare=input()
no=float(fare.replace("$",""))
nf=round(no/2+0.04, 1)
print("$", nf, sep="")
