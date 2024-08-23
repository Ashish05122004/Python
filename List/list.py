# we can store both string and Integer in a same list
list = [3,5,4,6,8,9,7];
list2 = [3,"ashish"];
list3 = ["a","d","e","b"];

# list.append(2); # it will add 2 at the end of list
# print(list);  

# list.sort();    # It will sort the elements present inside the list
# list3.sort();
# print(list);
# print(list3);

# list.sort(reverse=True); # It will reverse the order of sorting
# print(list);

# list.reverse(); #it will reverse the list
# print(list);

list.insert(0,20); #lsit.insert(idx,value) :It is used to insert an element at the given index
list.insert(0,1)
print(list);

# list4 = [3,2,1,4,1]
# list4.remove(1);# remove(value) :remove first occurrence of that value from the list
# print(list4);

# list4.pop(1); # pop(idx) :It removes the element which is at the given index
# print(list4);


# #List is mutable means we change the value at a given index:- e.g:
# l =[2,5,6,8];
# l[1] = 3;
# print(l);

# #but in case of string and tuple  we cannot do this because they are immutable.
# str = "Abcde";
# str[0]='n'; #error
# print(str);