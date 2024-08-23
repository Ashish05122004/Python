'''
Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programing in Java.
'''
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\n")
#     f.write("I like programing in Java.")



'''Q2.WAF that replace all occurrences of “Java” with “python” in above file.'''
def replace_word(old,new):
    with open("practice.txt","r") as f:
        data = f.read();
    new_data = data.replace(old,new)
    with open("practice.txt","r+") as f:
        f.write(new_data)

# replace_word("Java","Python")

'''Q3.Search if the word “learning” exists in the file or not.'''
def check_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        # print(data.find(word))

        # if(data.find(word) !=-1): 
        if(word in data):
            print(word,"is found")
        else:
            print(word,"is not found")

# check_word("learning")

'''Q4.WAF to find in which line of the file does the word “learning”occur first.Print -1 if word not found.'''
def check_for_line(word):
    line = 1
    with open("practice.txt","r") as f:
        data = True
        while data:
            data = f.readline()
            if(word in data):
                print(line)
                return
            line+=1
    print("-1")

        
# check_for_line("learning")

'''Q5.From a file containing numbers separated by comma, print the count of even numbers.'''
def check_Even_count1():
    c=0;
    with open("practice.txt","r") as f:
        data = f.read()
        num=""
        for i in data:
            if(i==","):
                # print(int(num))
                if(int(num)%2==0):
                    c+=1  
                num=""
            else:
                num+=i
    print(c)

def check_Even_count2():
    c=0
    with open("practice.txt","r") as f:
        data = f.read()
        list =data.split(",")
        print(list)
        for val in list:
            if(int(val)%2==0):
                c+=1
    print(c)

check_Even_count2()



