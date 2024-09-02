with open("file.txt","r") as f:
    content =f.read()
    with open("newFile.txt","w") as fr:
        fr.write(content)