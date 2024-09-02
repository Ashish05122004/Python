def generatetable(n):
    table =""
    for i in range(1,11):
        table+=f"{i} x {n} = {i*n}\n"
    with open(f"Practice_Sets/FileIo/table/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,13):
    generatetable(i)