
a = input("Enter a operand1 :");
b=input("Enter a operand2 :");
op = input("Enter the operator :");

if op == '+':
    print(int(a)+int(b));
elif op == '-':
    print(int(a)-int(b));
elif op == '*':
    print(int(a)*int(b));
elif op == '**':  #power
    print(int(a)**int(b));
elif op == '/':
    print(int(a)/int(b));
elif op == '//': #floor division
    print(int(a)//int(b));
else:
    print("Invalid operator");

x=3;
y="ashish";
print(x*y);