"""
Q1. Store following word meanings in a python dictionary :
"""
# meanas ={
#     "table": ["a piece of furniture","list of facts & figures"],
#     "cat":"a small animal"
# }

"""
Q2. You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”,“java”,“C++”,“python”,“javascript”,java”,“python”,“java”,“C++”,“C”
"""
# sub = set();
# sub.add("python")
# sub.add("java")
# sub.add("c++")
# sub.add("python")
# sub.add("js")
# sub.add("java")
# sub.add("python")
# sub.add("java")
# sub.add("c++")
# sub.add("c")

# print(len(sub));
# print(sub)

"""
Q3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
"""
# marks={};

# marks.update({input( "Enter subject name : "):int(input("Enter mark:"))})
# marks.update({input( "Enter subject name : "):int(input("Enter mark:"))})
# marks.update({input( "Enter subject name : "):int(input("Enter mark:"))})
# print(marks);

"""
Q4.Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
"""
s =set()
# s.add(9);
# s.add(9.0);

s1 = ("int",9);
s2 = ("float",9.0)
s.add(s1)
s.add(s2)
print(s);