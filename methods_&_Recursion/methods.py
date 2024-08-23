#syntax:
# def methodName(arg1,arg2):
#     task->
#     return

#e.g:-
def sum(a,b):
    return a+b
    
print(sum(3,5))

#Q1.factorial of a number:
def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i;
    return a;

print(fact(4))