#tuple is immutable so we can't change  the value of tuple but we can add or remove
tup = (1,3,4,5);
print(tup);
print(type(tup));

t =(1);
print(type(t));#int but t = (1,) is tuple

tup2 = ("ashish","manish","ankit","amon","ashish","ashish", "ashish");
# tup2.index(4);
print(tup2.index("ashish")); #it will give index of the element

print(tup2.count("ashish")); #it will give the occurence of the element