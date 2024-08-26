def rem(l,w):
    n=[]
    for i in l:
        if(not(i == w)):
            n.append(i.strip(w))
    return n
    
l =["ashish","harish","amon","ish"]
print(rem(l,"sh"))