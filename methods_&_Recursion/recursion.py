def fact(a):
    if(a==0 or a==1):
        return 1
    return a*fact(a-1)

print(fact(4))