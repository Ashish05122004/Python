#we can put anything in a dictionary like srting,int,list,tuple,dictionary etc...
#Dictionary is mutable we can change the value of the key like List
student = {
    "name":"ashish",
    "age":18,
    "isDict":True,
    "subject":["math","eng","phy"],
    "marks":{
        "math":95,
        "eng":80,
        "phy":93
    }
}
# print(type(student));
# print(student["name"]);
# print(student["subject"]);
# print(student["marks"]);
# print(student["marks"]["math"]);#imp

#? -------------------------------------------------------------->
#operations 
# print(len(student));

# #?1:insert
# new_dict = {"id":2,"dept":"IT","Date":"25-02-2024"};
# student.update({"city":"balasore"}); #Insert the key and value in a  dictionary
# student.update(new_dict);
# print(student);

# #?2:geting all keys
# print(student.keys()); #return all keys present in the dict

# #?3:getting all values of dictionary
# print(student.values()); # return all values

# #?geting items i.e. both key and value
# print(student.items()); # returns tuple containing key and its value
# print(list(student.items())); #converts items into list

# #?get the value of a perticular key
# print(student.get("name")); #more preferable because it will never give error..
# print(student["name"]); #It will give error if we pass wrong key..

# print(student.get("name2")); #gives the value if it exists otherwise None
# print(student["name2"]); #gives error