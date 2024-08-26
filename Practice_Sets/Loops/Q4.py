n=8
c=0
for i in range(2,int(n/2)):
    if(n%i == 0):
        c+=1
if(c==0):
    print("prime")
else:
    print("not prime")
