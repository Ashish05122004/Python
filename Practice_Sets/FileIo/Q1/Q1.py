with open("C:/Users/ashis/OneDrive/Desktop/Python/Practice_Sets/FileIo/poems.txt","r") as f:
    str = f.read()
    if("twinkle" in str):
        print("twinkle is present in the string")
    else:
        print("not present")