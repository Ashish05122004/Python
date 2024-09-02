with open("Practice_Sets/FileIo/file.txt","r") as f:
    s = f.read()
ns= s.replace("donkey","#####")
with open("Practice_Sets/FileIo/file.txt","w") as fr:
    fr.write(ns)
