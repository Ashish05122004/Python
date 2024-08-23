#we can write a string with " " and ' '
s1 = 'Ashish';
s2 = "kumar";

print("hello,", s1);  # hello,Ashish

# apple = 'he said,"I am a good boy"';
# # triple quotes allow us to have multiple lines in the string.
# apple2 = '''hii
# hello
# Namaskar!!!''';
# print(apple2); #''' ''' code for multiple string

# ----------------------------------------------------------------------------->


# #len(str): returns the length of the given string.
# print(len(apple));   # 25
# print(len(apple2)); # 21

# ----------------------------------------------------------------------------->

# # srting visiting each character
# for i in s1:
#     print(i);

# ----------------------------------------------------------------------------->

# #slicing a string 
# # syntax : str[start:end] where start is inclusive and end is exclusive.
# print(s1[0:4]) #Ashi
# print(s1[:4]) #Ashi

# print(s1[2:]) #hish ---->#end=len(s1)  by default

# print(s1[0:-3]); #i.e s1[0:len(s1)-3] =>S1[0:3]
#                     # Ashish -> Asi

# print(s1[-3:]); #i.e s1[len(s1)-3:] -->s1[3:6]
# print(s1[-3:-1]); #s1[3,5]

# #Quick Quiz
# nm = "Harry";
# print(nm[-4:-2]);

# ----------------------------------------------------------------------------->
# string methods : 

str = "i am a student. am am am am"

# #str.endswith("suffix"): returns true if String ends with substr
# print(str.endswith("ent"));

#print(str.count("am")) #counts the occurrence of substr in string

# print(str.capitalize( ))  #capitalizes 1st char


# print(str.replace( "a", "c" ) )#replaces all occurrences of old with new

print(str.find("am")) #returns 1st index of 1st occurrence