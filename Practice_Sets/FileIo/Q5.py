words =["donkey","balasore","boy"]
with open("Practice_Sets/FileIo/file.txt","r") as f:
    s = f.read()

for word in words:
    s= s.replace(word,"#"*len(word))
    
with open("Practice_Sets/FileIo/file.txt","w") as fr:
    fr.write(s)
